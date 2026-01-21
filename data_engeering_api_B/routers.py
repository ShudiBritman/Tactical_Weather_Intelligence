from fastapi import APIRouter, HTTPException
from schemas import WhatherLocation
from service import DataProcess


router = APIRouter()


@router.post("/clean")
def clean_data_route(data: WhatherLocation):
    print(data)
    return DataProcess.clean_data(data)
