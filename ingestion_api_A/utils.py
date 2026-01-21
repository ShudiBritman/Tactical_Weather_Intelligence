
import requests

def fetch_coordinates(location_name: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    
    params = {
        "name": location_name,
        "count": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError(f"Location not found: {location_name}")

    result = data["results"][0]
    return {
        "location_name": result["name"],
        "country": result.get("country"),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }

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

