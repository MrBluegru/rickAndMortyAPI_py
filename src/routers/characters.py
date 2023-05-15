from fastapi import APIRouter

router = APIRouter(prefix="/characters",
                   tags=["/characters"], responses={404: {"message": "No encontrado"}})


@router.get("/all")
async def characters():
    return ["Characters 1", "Characters 2", "Characters 3", "Characters 4", "Characters 5", "Characters 6",
            ]
