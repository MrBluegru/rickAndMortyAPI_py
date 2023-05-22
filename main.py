import requests
from fastapi import FastAPI
from src.routers import characters, episodes
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
CORS = os.getenv("CORS")

# Routers
app.include_router(characters.router)
app.include_router(episodes.router)
app.mount("/static", StaticFiles(directory="static"), name='static')
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    image_url = "https://www.vodafone.es/c/statics/imagen/img_OG_Rick_y_Morty_T4_V2.jpg"
    response = requests.get(image_url)
    return Response(content=response.content, media_type="image/jpeg")
