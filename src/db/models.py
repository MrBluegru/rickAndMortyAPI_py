from sqlalchemy import Table, Column, String, ForeignKey, UUID
from src.db.database import Base
from sqlalchemy.orm import relationship

character_episode = Table('character_episode', Base.metadata,
                          Column('character_id', UUID,
                                 ForeignKey('characters.id')),
                          Column('episode_id', UUID, ForeignKey('episodes.id'))
                          )

class Character(Base):
    __tablename__ = "characters"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    species = Column(String)
    gender = Column(String)
    origin = Column(String)
    location = Column(String)
    image = Column(String)
    episodes = relationship(
        "Episode", secondary=character_episode, back_populates="characters")


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, index=True)
    air_date = Column(String)
    episode = Column(String)
    characters = relationship(
        "Character", secondary=character_episode, back_populates="episodes")
