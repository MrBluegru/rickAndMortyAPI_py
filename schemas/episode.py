from pydantic import BaseModel
from typing import Optional


class Episode(BaseModel):
    id: Optional[str]
    name: str
    air_date: str
    episode: str
   
