from app3 import app


def test_register_user():
    client = app.test_client()

    response = client.post(
        "/register",
        json={
            "username": "alice",
            "password": "5678"
        }
    )

    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"


def test_register_without_data():
    client = app.test_client()

    response = client.post("/register")

    assert response.status_code == 400
    assert response.json["error"] == "Request body is required"


def test_register_without_username():
    client = app.test_client()

    response = client.post(
        "/register",
        json={
            "password": "1234"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "Username and password are required"


def test_register_without_password():
    client = app.test_client()

    response = client.post(
        "/register",
        json={
            "username": "alice"
        }
    )

    assert response.status_code == 400
    assert response.json["error"] == "Username and password are required"


def test_register_existing_user():
    client = app.test_client()

    response = client.post(
        "/register",
        json={
            "username": "john",
            "password": "1234"
        }
    )

    assert response.status_code == 409
    assert response.json["error"] == "User already exists"


def test_login_success():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "username": "john",
            "password": "1234"
        }
    )

    assert response.status_code == 200
    assert response.json["message"] == "Login successful"


def test_login_wrong_password():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "username": "john",
            "password": "wrong"
        }
    )

    assert response.status_code == 401
    assert response.json["error"] == "Invalid username or password"


def test_profile_without_login():
    client = app.test_client()

    response = client.get("/profile")

    assert response.status_code == 401
    assert response.json["error"] == "Unauthorized"


def test_profile_after_login():
    client = app.test_client()

    client.post(
        "/login",
        json={
            "username": "john",
            "password": "1234"
        }
    )

    response = client.get("/profile")

    assert response.status_code == 200
    assert response.json["username"] == "john"


def test_logout():
    client = app.test_client()

    client.post(
        "/login",
        json={
            "username": "john",
            "password": "1234"
        }
    )

    response = client.post("/logout")

    assert response.status_code == 200
    assert response.json["message"] == "Logout successful"


def test_profile_after_logout():
    client = app.test_client()

    client.post(
        "/login",
        json={
            "username": "john",
            "password": "1234"
        }
    )

    client.post("/logout")

    response = client.get("/profile")

    assert response.status_code == 401
    assert response.json["error"] == "Unauthorized"