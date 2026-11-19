from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    """Vérifie que la route /health répond 200 et respecte le format attendu."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "version" in data
    assert "commit" in data
    assert "database" in data

def test_order_negative_or_zero_quantity():
    """Vérifie que la commande d'une quantité <= 0 est refusée avec une erreur 400."""
    response = client.post("/orders", json={"product_id": 1, "quantity": 0})
    assert response.status_code == 400

    response_neg = client.post("/orders", json={"product_id": 1, "quantity": -5})
    assert response_neg.status_code == 400
