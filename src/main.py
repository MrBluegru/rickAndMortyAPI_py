import requests
from fastapi import FastAPI
from routers import characters, episodes
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response

app = FastAPI()

# Routers
app.include_router(characters.router)
app.include_router(episodes.router)
app.mount("/static", StaticFiles(directory="static"), name='static')


@app.get("/")
async def root():
    image_url = "https://www.vodafone.es/c/statics/imagen/img_OG_Rick_y_Morty_T4_V2.jpg"
    response = requests.get(image_url)
    return Response(content=response.content, media_type="image/jpeg")
