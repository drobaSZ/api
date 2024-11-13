import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get("/api/items")
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_item(client):
    response = client.get("/api/items/1")
    assert response.status_code == 200
    assert response.json["id"] == 1

def test_create_item(client):
    response = client.post("/api/items", json={"name": "New Item"})
    assert response.status_code == 201
    assert response.json["name"] == "New Item"

def test_update_item(client):
    response = client.put("/api/items/1", json={"name": "Updated Item"})
    assert response.status_code == 200
    assert response.json["name"] == "Updated Item"

def test_delete_item(client):
    response = client.delete("/api/items/1")
    assert response.status_code == 200
    assert response.json["message"] == "Item deleted"

