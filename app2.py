from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 1000},
    {"id": 3, "name": "Keyboard", "price": 2000}
]


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    if "name" not in data or "price" not in data:
        return jsonify({"error": "Name and price are required"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    products.append(new_product)

    return jsonify(new_product), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    for product in products:
        if product["id"] == product_id:

            if "name" in data:
                product["name"] = data["name"]

            if "price" in data:
                product["price"] = data["price"]

            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    for product in products:
        if product["id"] == product_id:

            products.remove(product)

            return jsonify({
                "message": "Product deleted successfully"
            })

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)