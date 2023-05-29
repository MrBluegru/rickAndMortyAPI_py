from fastapi import APIRouter, HTTPException
from src.api.episodesApi import get_episodes_of_api

router = APIRouter(prefix="/episodes",
                   tags=["/episodes"], responses={404: {"message": "No encontrado"}})


@router.get("/all")
async def episodes():
    try:
        return get_episodes_of_api()
    except Exception as exception:
        raise HTTPException(
            status_code=404, detail=f'Error {exception}'
        )
