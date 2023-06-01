from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

characters = Table("characters", meta, Column("id", Integer, primary_key=True),
                  Column("name", String(255)),
                  Column("status", String(255)),
                  Column("species", String(255)),
                  Column("gender", String(255)),
                  Column("origin", String(255)),
                  Column("location", String(255)),
                  Column("image", String(255))
                  )

meta.create_all(engine)
