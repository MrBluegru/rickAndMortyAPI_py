from fastapi import APIRouter, HTTPException
import aiohttp


router = APIRouter(prefix="/characters",
                   tags=["/characters"], responses={404: {"message": "No encontrado"}})


@router.get("/{nroPage}")
async def characters(nroPage: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://rickandmortyapi.com/api/character?page={nroPage}") as response:
            try:
                data = await response.json()
                characters = data["results"]
                mapped_data = list(map(lambda character: {
                    "name": character["name"],
                    "status": character["status"],
                    "species": character["species"],
                    "gender": character["gender"],
                    "origin": character["origin"]["name"],
                    "location": character["location"]["name"],
                    "image": character["image"],
                }, characters))
                return mapped_data
            except Exception as exception:
                raise HTTPException(
                    status_code=404, detail=f'Error {exception}'
                )
