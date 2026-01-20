from fastapi import APIRouter, HTTPException
from schemas import WhetherLocation
from service import clean_data


router = APIRouter()


@router.post("/clean")
def clean_data_route(data: WhetherLocation):
    try:
        return clean_data(data)
    except Exception as e:
        raise{"message": e}
