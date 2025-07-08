from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_earn():
    response = client.post("/earns/", json={
        "earn_name": "Salário",
        "amount": 1000,
        "earn_way": "PIX"
    })
    assert response.status_code == 201
    assert response.json()["received"]["earn_name"] == "Salário"
