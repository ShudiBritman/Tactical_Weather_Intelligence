

import requests


def fetch_hourly_weather(latitude: float, longitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
        "past_days": 1,
        "timezone": "UTC"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["hourly"]

