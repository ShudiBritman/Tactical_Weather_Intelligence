from fastapi import APIRouter, HTTPException



router = APIRouter()


@router.post("/clean")
def clean_data(data):
    pass