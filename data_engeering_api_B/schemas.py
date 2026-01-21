from pydantic import BaseModel, Field
from typing import Annotated
import datetime



class WhetherLocation(BaseModel):
    timestamp: datetime
    location_name: str
    country: str
    latitude: Annotated[float, Field(
        ge=-90,
        le=90
    )]
    longitude: Annotated[float, Field(
        ge=-180,
        le=180
    )]
    temperature: Annotated[float, Field(
        ge=-100,
        le=70
    )]
    wind_speed: float
    humidity: float