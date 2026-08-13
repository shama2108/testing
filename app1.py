from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello World"
    })


@app.route("/users", methods=["GET"])
def get_users():
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"},
        {"id": 3, "name": "Bob"}
    ]

    return jsonify(users)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"},
        {"id": 3, "name": "Bob"}
    ]

    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404


@app.route("/add", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    user = {
        "id": 4,
        "name": data["name"]
    }

    return jsonify(user), 201


if __name__ == "__main__":
    app.run(debug=True)