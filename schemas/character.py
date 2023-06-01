from pydantic import BaseModel
from typing import Optional


class Character(BaseModel):
    id: Optional[str]
    name: str
    status: str
    species: str
    gender: str
    origin: str
    location: str
    image: str
