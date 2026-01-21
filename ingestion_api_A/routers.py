from fastapi import APIRouter, HTTPException
from services import WeatherIngestor , send_to_engineering

router = APIRouter()

@router.get("/location/{location_name}")
def create_weather_for_location(location_name: str):
    try:
        ingestor = WeatherIngestor(location_name)
        records = ingestor.build_records()
        return send_to_engineering(records)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
