import uuid
from fastapi import APIRouter, HTTPException
from api.charactersApi import get_characters_of_api
from config.database import conn
from models.character import characters
from schemas.character import Character
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/characters",
    tags=["/characters"],
    responses={404: {"message": "Not found"}},
)


@router.get("/all")
def get_all_db_characters():
    try:
        characters_db = conn.execute(characters.select()).fetchall()

        if not characters_db:
            return {"message": "No characters in DB"}

        mapped_characters = list(
            map(
                lambda character: {
                    "id": character[0],
                    "name": character[1],
                    "status": character[2],
                    "species": character[3],
                    "gender": character[4],
                    "origin": character[5],
                    "location": character[6],
                    "image": character[7],
                },
                characters_db,
            )
        )
        return mapped_characters

    except Exception as exception:
        raise HTTPException(status_code=404, detail=f"Error {exception}")


@router.post("/new")
def create_new_character(char: Character):
    id = char.id if char.id is not None else str(uuid.uuid4())

    new_character = {
                "id": id,
                "name":char.name,
                "status":char.status,
                "species":char.species,
                "gender":char.gender,
                "origin":char.origin,
                "location":char.location,
                "image":char.image,
            }
    try:
        result = conn.execute(
            characters.insert().values(new_character)
        )
        conn.commit()
        if result.inserted_primary_key != 0:
            return {"message": "Character created successfully"}

    except Exception as exception:
        raise HTTPException(status_code=404, detail=f"Error: {exception}")
