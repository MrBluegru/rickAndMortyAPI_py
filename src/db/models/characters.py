from sqlalchemy import Column, Integer, String
from database import Base

class Characters(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    species = Column(String)
    gender = Column(String)
    origin = Column(String)
    location = Column(String)
    image = Column(String)