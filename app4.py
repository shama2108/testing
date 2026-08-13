from flask import Flask, jsonify

import requests

app = Flask(__name__)


@app.route("/weather/<city>", methods=["GET"])
def get_weather(city):

    url = f"https://api.example.com/weather/{city}"

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({
            "error": "Unable to fetch weather"
        }), 503

    data = response.json()

    return jsonify({
        "city": city,
        "temperature": data["temperature"],
        "condition": data["condition"]
    })


@app.route("/exchange-rate/<currency>", methods=["GET"])
def get_exchange_rate(currency):

    url = f"https://api.example.com/exchange/{currency}"

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({
            "error": "Unable to fetch exchange rate"
        }), 503

    data = response.json()

    return jsonify({
        "currency": currency,
        "rate": data["rate"]
    })


if __name__ == "__main__":
    app.run(debug=True)