import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import get_connection, check_db_health, init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialisation automatique des tables au démarrage si la BDD est prête."""
    try:
        init_db()
    except Exception:
        # En mode test ou si la base n'est pas encore prête, on ne bloque pas le démarrage
        pass
    yield

app = FastAPI(
    title="Producteurs & Restaurants API",
    version=os.getenv("APP_VERSION", "v1.1.0"),
    description="API minimale pour la gestion des commandes et stocks (TP DevOps M1 - US-42)",
    lifespan=lifespan
)

# Modèles Pydantic pour la validation
class OrderCreate(BaseModel):
    product_id: int
    quantity: int

class StockUpdate(BaseModel):
    stock: int

@app.get("/health")
def health():
    """Route de santé (Règle des 10 secondes du T3)."""
    db_ok = check_db_health()
    return {
        "status": "ok",
        "version": os.getenv("APP_VERSION", "v1.1.0"),
        "commit": os.getenv("APP_COMMIT", "dev"),
        "database": "connected" if db_ok else "unavailable"
    }

@app.get("/products")
def get_products(limit: int = 50):
    """Retourne la liste des produits disponibles."""
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, price, stock FROM products ORDER BY id ASC LIMIT %s;", (limit,))
            products = cur.fetchall()
        conn.close()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur base de donnees: {str(e)}")

@app.patch("/products/{product_id}/stock")
def update_product_stock(product_id: int, payload: StockUpdate):
    """Permet au producteur de déclarer ou mettre à jour le stock d'un produit (US-42)."""
    if payload.stock < 0:
        raise HTTPException(status_code=400, detail="Le stock ne peut pas etre negatif.")

    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, price, stock FROM products WHERE id = %s;", (product_id,))
            product = cur.fetchone()
            if not product:
                conn.close()
                raise HTTPException(status_code=404, detail="Produit non trouve.")

            cur.execute(
                "UPDATE products SET stock = %s WHERE id = %s RETURNING id, name, price, stock;",
                (payload.stock, product_id)
            )
            updated = cur.fetchone()
        conn.commit()
        conn.close()
        return updated
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur mise a jour stock: {str(e)}")

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    """Crée une commande pour un produit avec vérification et décrémentation du stock (US-42)."""
    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="La quantite doit etre superieure a zero.")

    try:
        conn = get_connection()
        with conn.cursor() as cur:
            # Vérifier si le produit existe
            cur.execute("SELECT id, name, stock FROM products WHERE id = %s;", (order.product_id,))
            product = cur.fetchone()
            if not product:
                conn.close()
                raise HTTPException(status_code=404, detail="Produit non trouve.")

            current_stock = product["stock"]

            # Vérifier si la commande dépasse le stock disponible (Règle US-42)
            if order.quantity > current_stock:
                conn.close()
                raise HTTPException(
                    status_code=400,
                    detail=f"Stock insuffisant : quantite demandee ({order.quantity}) superieure au stock disponible ({current_stock})."
                )

            # Décrémentation atomique du stock
            cur.execute(
                "UPDATE products SET stock = stock - %s WHERE id = %s;",
                (order.quantity, order.product_id)
            )

            # Insertion de la commande
            cur.execute(
                "INSERT INTO orders (product_id, quantity) VALUES (%s, %s) RETURNING id, created_at;",
                (order.product_id, order.quantity)
            )
            created = cur.fetchone()
        conn.commit()
        conn.close()

        return {
            "order_id": created["id"],
            "product_id": order.product_id,
            "quantity": order.quantity,
            "remaining_stock": current_stock - order.quantity,
            "created_at": created["created_at"]
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la commande: {str(e)}")
