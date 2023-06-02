import uuid
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String
from config.database import meta, engine

characters = Table(
    "characters",
    meta,
    Column(
        "id", String(36), primary_key=True, default=str(uuid.uuid4())
    ),
    Column("name", String(255)),
    Column("status", String(255)),
    Column("species", String(255)),
    Column("gender", String(255)),
    Column("origin", String(255)),
    Column("location", String(255)),
    Column("image", String(255)),
)

meta.create_all(engine)