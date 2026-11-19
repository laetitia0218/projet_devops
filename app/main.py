
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.db import get_connection, check_db_health, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialisation des tables au démarrage."""
    try:
        init_db()
    except Exception:
        # Ne bloque pas le démarrage en mode test.
        pass
    yield


app = FastAPI(
    title="Producteurs & Restaurants API",
    version=os.getenv("APP_VERSION", "v1.1.0"),
    description="API de gestion des commandes et stocks (TP DevOps M1 - US-42)",
    lifespan=lifespan,
)


class OrderCreate(BaseModel):
    product_id: int
    quantity: int


class StockUpdate(BaseModel):
    stock: int


@app.get("/health")
def health():
    """Vérifie la santé de l'API et de PostgreSQL."""
    db_ok = check_db_health()

    return {
        "status": "ok",
        "version": os.getenv("APP_VERSION", "v1.1.0"),
        "commit": os.getenv("APP_COMMIT", "dev"),
        "database": "connected" if db_ok else "unavailable",
    }


@app.get("/products")
def get_products(limit: int = 50):
    """Retourne les produits disponibles."""
    if limit < 1 or limit > 1200:
        raise HTTPException(
            status_code=400,
            detail="La limite doit etre comprise entre 1 et 1200.",
        )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, name, price, stock
                    FROM products
                    ORDER BY id ASC
                    LIMIT %s;
                    """,
                    (limit,),
                )
                return cur.fetchall()

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la recuperation des produits.",
        )


@app.patch("/products/{product_id}/stock")
def update_product_stock(product_id: int, payload: StockUpdate):
    """Déclare ou met à jour le stock d'un produit."""
    if payload.stock < 0:
        raise HTTPException(
            status_code=400,
            detail="Le stock ne peut pas etre negatif.",
        )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE products
                    SET stock = %s
                    WHERE id = %s
                    RETURNING id, name, price, stock;
                    """,
                    (payload.stock, product_id),
                )

                updated = cur.fetchone()

                if updated is None:
                    raise HTTPException(
                        status_code=404,
                        detail="Produit non trouve.",
                    )

                return updated

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la mise a jour du stock.",
        )


@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    """
    Crée une commande et décrémente le stock de manière atomique.
    Empêche deux commandes simultanées de provoquer une survente.
    """
    if order.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="La quantite doit etre superieure a zero.",
        )

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:

                # Décrémentation atomique uniquement si le stock suffit.
                cur.execute(
                    """
                    UPDATE products
                    SET stock = stock - %s
                    WHERE id = %s
                      AND stock >= %s
                    RETURNING stock;
                    """,
                    (
                        order.quantity,
                        order.product_id,
                        order.quantity,
                    ),
                )

                updated = cur.fetchone()

                if updated is None:
                    # Distinguer un produit inexistant d'un stock insuffisant.
                    cur.execute(
                        """
                        SELECT stock
                        FROM products
                        WHERE id = %s;
                        """,
                        (order.product_id,),
                    )

                    product = cur.fetchone()

                    if product is None:
                        raise HTTPException(
                            status_code=404,
                            detail="Produit non trouve.",
                        )

                    raise HTTPException(
                        status_code=400,
                        detail=(
                            "Stock insuffisant : quantite demandee "
                            f"({order.quantity}) superieure au stock "
                            f"disponible ({product['stock']})."
                        ),
                    )

                remaining_stock = updated["stock"]

                # Commande et stock dans la même transaction.
                cur.execute(
                    """
                    INSERT INTO orders (product_id, quantity)
                    VALUES (%s, %s)
                    RETURNING id, created_at;
                    """,
                    (order.product_id, order.quantity),
                )

                created = cur.fetchone()

                return {
                    "order_id": created["id"],
                    "product_id": order.product_id,
                    "quantity": order.quantity,
                    "remaining_stock": remaining_stock,
                    "created_at": created["created_at"],
                }

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la creation de la commande.",
        )
