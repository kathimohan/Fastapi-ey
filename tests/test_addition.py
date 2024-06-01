import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_addition():
    response = client.post("/api/add", json={
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"

def test_addition_with_empty_payload():
    response = client.post("/api/add", json={
        "batchid": "id0101",
        "payload": []
    })
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == []
    assert data["status"] == "complete"

def test_addition_with_invalid_data():
    response = client.post("/api/add", json={
        "batchid": "id0101",
        "payload": "invalid"
    })
    assert response.status_code == 422
