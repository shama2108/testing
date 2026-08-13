from app4 import app
from unittest.mock import patch, Mock


def test_weather_success():
    client = app.test_client()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "temperature": 25,
        "condition": "Sunny"
    }

    with patch("app4.requests.get", return_value=mock_response) as mock_get:
        response = client.get("/weather/Indore")

    assert response.status_code == 200
    assert response.json["city"] == "Indore"
    assert response.json["temperature"] == 25
    assert response.json["condition"] == "Sunny"

    mock_get.assert_called_once_with(
        "https://api.example.com/weather/Indore"
    )


def test_weather_api_failure():
    client = app.test_client()

    mock_response = Mock()
    mock_response.status_code = 500

    with patch("app4.requests.get", return_value=mock_response) as mock_get:
        response = client.get("/weather/Indore")

    assert response.status_code == 503
    assert response.json["error"] == "Unable to fetch weather"

    mock_get.assert_called_once_with(
        "https://api.example.com/weather/Indore"
    )


def test_weather_different_city():
    client = app.test_client()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "temperature": 30,
        "condition": "Cloudy"
    }

    with patch("app4.requests.get", return_value=mock_response):
        response = client.get("/weather/Mumbai")

    assert response.status_code == 200
    assert response.json["city"] == "Mumbai"
    assert response.json["temperature"] == 30
    assert response.json["condition"] == "Cloudy"


def test_exchange_rate_success():
    client = app.test_client()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rate": 83.50
    }

    with patch("app4.requests.get", return_value=mock_response) as mock_get:
        response = client.get("/exchange-rate/USD")

    assert response.status_code == 200
    assert response.json["currency"] == "USD"
    assert response.json["rate"] == 83.50

    mock_get.assert_called_once_with(
        "https://api.example.com/exchange/USD"
    )


def test_exchange_rate_failure():
    client = app.test_client()

    mock_response = Mock()
    mock_response.status_code = 500

    with patch("app4.requests.get", return_value=mock_response) as mock_get:
        response = client.get("/exchange-rate/USD")

    assert response.status_code == 503
    assert response.json["error"] == "Unable to fetch exchange rate"

    mock_get.assert_called_once_with(
        "https://api.example.com/exchange/USD"
    )


def test_exchange_rate_different_currency():
    client = app.test_client()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rate": 91.25
    }

    with patch("app4.requests.get", return_value=mock_response):
        response = client.get("/exchange-rate/EUR")

    assert response.status_code == 200
    assert response.json["currency"] == "EUR"
    assert response.json["rate"] == 91.25