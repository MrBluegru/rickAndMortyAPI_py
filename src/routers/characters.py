from fastapi import APIRouter, HTTPException
from src.api.charactersApi import get_characters_of_api

router = APIRouter(prefix="/characters",
                   tags=["/characters"], responses={404: {"message": "No encontrado"}})


@router.get("/all")
def characters():
    try:
        data = get_characters_of_api()
        return data
    except Exception as exception:
        raise HTTPException(
            status_code=404, detail=f'Error {exception}'
        )
