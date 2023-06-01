from cgitb import text
from sqlalchemy import select
from fastapi import APIRouter, HTTPException
from api.charactersApi import get_characters_of_api
from config.database import conn
from models.character import characters
from models.episode import episodes
from schemas.character import Character
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/characters",
                   tags=["/characters"], responses={404: {"message": "No encontrado"}})

@router.get("/all")
def all_characters():
    try:
        return get_characters_of_api()
    except Exception as exception:
        raise HTTPException(
            status_code=404, detail=f'Error {exception}'
        )


@router.get("/db")
def get_db_characters():
    charactersDB = conn.execute(characters.select()).fetchall()
    # character_list = [dict(c) for c in charactersDB]
    print (charactersDB)

@router.get("/epi")
def get_db_episodes():
    charactersDB = conn.execute(episodes.select()).fetchall()
    character_list = [dict(c) for c in charactersDB]
    return JSONResponse(content=character_list)


@router.post("/characters")
def create_character(char: Character):
    new_character = char.dict()
    try:
        # Insert the new character into the "characters" table
        result = conn.execute(characters.insert().values(new_character))
        conn.commit() # Agregar esta instrucción para guardar los cambios en la base de datos
        print(f"Se insertó correctamente el registro con id {result.inserted_primary_key}")
        return {"message": "Character created successfully"}
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
        raise HTTPException(status_code=500, detail="Error al insertar el registro")

@router.get("/test")
def test_db():
    try:
        query = select([characters]).select_from(characters.table)
        result = conn.execute(query)
        return {'message': 'Database connection successful'}
    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")