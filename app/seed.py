import os
import random
from app.db import get_connection, init_db

PRODUCT_CATEGORIES = [
    "Pommes", "Poires", "Tomates", "Carottes", "Salades",
    "Courgettes", "Pommes de terre", "Oignons", "Fromage de chevre",
    "Miel", "Pain artisanal", "Oeufs bio", "Farine de ble", "Lait frais"
]

def seed_products(count: int = 1200):
    """Insère count (1200) produits initiaux dans la base PostgreSQL."""
    print(f"--- Initialisation des tables ---")
    init_db()

    conn = get_connection()
    with conn.cursor() as cur:
        # Vérifier si la table a déjà des produits
        cur.execute("SELECT COUNT(*) AS total FROM products;")
        total_existing = cur.fetchone()["total"]

        if total_existing >= count:
            print(f"La base contient deja {total_existing} produits. Pas besoin de re-peupler.")
            conn.close()
            return

        print(f"Insertion de {count} produits initiaux en base...")
        products_data = []
        for i in range(1, count + 1):
            category = random.choice(PRODUCT_CATEGORIES)
            name = f"{category} #{i:04d}"
            price = round(random.uniform(1.5, 35.0), 2)
            stock = random.randint(10, 200)
            products_data.append((name, price, stock))

        # Insertion groupée pour aller très vite
        cur.executemany(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s);",
            products_data
        )
    conn.commit()
    conn.close()
    print(f"Succès : {count} produits inseres avec succes !")

if __name__ == "__main__":
    seed_products(1200)
