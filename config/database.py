import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from utils.msj import *

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_PORT}/{DB_NAME}")

meta = MetaData()

conn = engine.connect()

