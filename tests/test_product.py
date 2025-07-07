from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_product_success():
    response = client.get("/product/1")
    assert response.status_code == 200
    assert "title" in response.json()

def test_get_product_not_found():
    response = client.get("/product/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_get_all_products():
    response = client.get("/product/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_related_products():
    response = client.get("/product/1/related")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_products_from_seller():
    response = client.get("/product/1/1/from-seller")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
