from fastapi import APIRouter

router = APIRouter(prefix="/episodes",
                   tags=["/episodes"], responses={404: {"message": "No encontrado"}})


@router.get("/all")
async def episodes():
    return ["Episode 1", "Episode 2", "Episode 3", "Episode 4", "Episode 5", "Episode 6",
            ]
