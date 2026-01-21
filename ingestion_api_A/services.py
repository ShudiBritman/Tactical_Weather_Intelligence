from datetime import datetime
from utils import *
import os

class WeatherIngestor:
    def __init__(self, location_name: str):
        self.location_name = location_name

    def build_records(self) -> list[dict]:
        location = fetch_coordinates(self.location_name)
        hourly = fetch_hourly_weather(
            location["latitude"],
            location["longitude"]
        )

        records = []
        for i, time in enumerate(hourly["time"]):
            records.append({
                "timestamp": time,
                "location_name": location["location_name"],
                "country": location["country"],
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "temperature": hourly["temperature_2m"][i],
                "wind_speed": hourly["wind_speed_10m"][i],
                "humidity": hourly["relative_humidity_2m"][i],
            })
        return records

def send_to_engineering(records: list[dict]):
    url = os.getenv("SERVICE_B_URL")
    response = requests.post(url, json={"records": records})
    response.raise_for_status()
    return response.json()
