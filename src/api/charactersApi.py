import asyncio
import requests
from typing import List

async def getInfAPI() -> List[dict]:
  nroPages = 42
  links = [f"https://rickandmortyapi.com/api/character?page={i}" for i in range(1, nroPages+1)]

  data = await asyncio.gather(*(requests.get(link) for link in links))
  mapped = [item for sublist in [res.json()['results'] for res in data] for item in sublist]
  mapped = [
    {
      'id': e['id'],
      'name': e['name'],
      'status': e['status'],
      'species': e['species'],
      'origin': e['origin']['name'],
      'image': e['image'],
      'created': e['created']
    } for e in mapped
  ]
  return mapped