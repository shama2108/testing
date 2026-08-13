from flask import Flask, jsonify, request, session

app = Flask(__name__)

app.secret_key = "test-secret-key"

users = [
    {
        "id": 1,
        "username": "john",
        "password": "1234"
    }
]


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "username" not in data or "password" not in data:
        return jsonify({
            "error": "Username and password are required"
        }), 400

    for user in users:
        if user["username"] == data["username"]:
            return jsonify({
                "error": "User already exists"
            }), 409

    new_user = {
        "id": len(users) + 1,
        "username": data["username"],
        "password": data["password"]
    }

    users.append(new_user)

    return jsonify({
        "message": "User registered successfully"
    }), 201


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:

            session["user_id"] = user["id"]

            return jsonify({
                "message": "Login successful"
            }), 200

    return jsonify({
        "error": "Invalid username or password"
    }), 401


@app.route("/profile", methods=["GET"])
def profile():

    if "user_id" not in session:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    user_id = session["user_id"]

    for user in users:
        if user["id"] == user_id:
            return jsonify({
                "id": user["id"],
                "username": user["username"]
            })

    return jsonify({
        "error": "User not found"
    }), 404


@app.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "message": "Logout successful"
    })


if __name__ == "__main__":
    app.run(debug=True)