from app2 import app




def test_get_products():
    client = app.test_client()

    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json) >= 1


def test_get_product():
    client = app.test_client()

    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json["name"] == "Laptop"


def test_product_not_found():
    client = app.test_client()

    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json["error"] == "Product not found"


def test_create_product():
    client = app.test_client()

    response = client.post(
        "/products",
        json={
            "name": "Monitor",
            "price": 15000
        }
    )

    assert response.status_code == 201
    assert response.json["name"] == "Monitor"
    assert response.json["price"] == 15000


def test_create_product_without_data():
    client = app.test_client()

    response = client.post(
        "/products",
        json={}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Request body is required"


def test_create_product_without_price():
    client = app.test_client()

    response = client.post(
        "/products",
        json={
            "name": "Monitor"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "Name and price are required"


def test_update_product():
    client = app.test_client()

    response = client.put(
        "/products/1",
        json={
            "name": "Gaming Laptop",
            "price": 70000
        }
    )

    assert response.status_code == 200
    assert response.json["name"] == "Gaming Laptop"
    assert response.json["price"] == 70000


def test_update_product_not_found():
    client = app.test_client()

    response = client.put(
        "/products/999",
        json={
            "name": "Test Product"
        }
    )

    assert response.status_code == 404
    assert response.json["error"] == "Product not found"


def test_delete_product():
    client = app.test_client()

    response = client.delete("/products/3")

    assert response.status_code == 200
    assert response.json["message"] == "Product deleted successfully"