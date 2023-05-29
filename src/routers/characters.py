from fastapi import APIRouter, HTTPException
from src.api.charactersApi import get_characters_of_api
from sqlalchemy.orm import Session
from src.db.models import Character, Episode
from src.validateTypes.characters_create import CharacterCreate
from typing import List

router = APIRouter(prefix="/characters",
                   tags=["/characters"], responses={404: {"message": "No encontrado"}})


@router.get("/all")
def characters():
    try:
        return get_characters_of_api()
    except Exception as exception:
        raise HTTPException(
            status_code=404, detail=f'Error {exception}'
        )


# @router.post("/create/")
# def create_character_with_episodes(character: CharacterCreate, episode_ids: List[int], db: Session):
#     db_character = Character(**character.dict())

#     db.add(db_character)
#     db.commit()
#     db.refresh(db_character)

#     return db_character
