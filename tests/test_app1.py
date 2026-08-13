from app1 import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Hello World"


def test_get_users():
    client = app.test_client()

    response = client.get("/users")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_user():
    client = app.test_client()

    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json["name"] == "John"


def test_user_not_found():
    client = app.test_client()

    response = client.get("/users/99")

    assert response.status_code == 404
    assert response.json["error"] == "User not found"


def test_add_user():
    client = app.test_client()

    response = client.post(
        "/add",
        json={"name": "David"}
    )

    assert response.status_code == 201
    assert response.json["name"] == "David"


def test_add_user_without_name():
    client = app.test_client()

    response = client.post(
        "/add",
        json={}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Name is required"