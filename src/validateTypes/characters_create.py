from typing import List
from pydantic import BaseModel

class CharacterCreate(BaseModel):
    name: str
    status: str
    species: str
    gender: str
    origin: str
    location: str
    image: str
    groups: List[str] = []