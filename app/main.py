import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import get_connection, check_db_health, init_db

app = FastAPI(
    title="Producteurs & Restaurants API",
    version=os.getenv("APP_VERSION", "v1.0.0"),
    description="API minimale pour la gestion des commandes et produits (TP DevOps M1)"
)

# Modèle pour la création de commande
class OrderCreate(BaseModel):
    product_id: int
    quantity: int

@app.on_event("startup")
def startup_event():
    """Initialisation automatique des tables au démarrage si la BDD est prête."""
    try:
        init_db()
    except Exception:
        # En mode test ou si la base n'est pas encore prête, on ne bloque pas le démarrage
        pass

@app.get("/health")
def health():
    """Route de santé (Règle des 10 secondes du T3)."""
    db_ok = check_db_health()
    return {
        "status": "ok",
        "version": os.getenv("APP_VERSION", "v1.0.0"),
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

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    """Crée une commande pour un produit donné."""
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

            # Créer la commande
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
            "created_at": created["created_at"]
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la commande: {str(e)}")
