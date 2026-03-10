from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict():
    response = client.post(
        "/predict",
        json={"age": 25, "income": 5000}
    )

    assert response.status_code == 200
    assert "prediction" in response.json()