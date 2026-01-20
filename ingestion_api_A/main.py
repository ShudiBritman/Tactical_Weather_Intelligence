import requests
from datetime import datetime
from fetch_coordinates import *
from fetch_hourly_weather import *


# --------- Main Ingestion Logic ----------
def ingest_weather_for_locations(locations):
    records = []

    for location_name in locations:
        location = fetch_coordinates(location_name)
        hourly_data = fetch_hourly_weather(
            location["latitude"],
            location["longitude"]
        )

        times = hourly_data["time"]
        temperatures = hourly_data["temperature_2m"]
        wind_speeds = hourly_data["wind_speed_10m"]
        humidities = hourly_data["relative_humidity_2m"]

        # 3. Flatten to records (ONE record per hour per location)
        for i in range(len(times)):
            record = {
                "timestamp": datetime.fromisoformat(times[i]),
                "location_name": location["location_name"],
                "country": location["country"],
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "temperature": temperatures[i],
                "wind_speed": wind_speeds[i],
                "humidity": humidities[i]

            }
            records.append(record)

    return records

