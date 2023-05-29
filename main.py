import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from src.routers import characters, episodes
from fastapi.middleware.cors import CORSMiddleware

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
    return FileResponse("static/init.jpeg")
