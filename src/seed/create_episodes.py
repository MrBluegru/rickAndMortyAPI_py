from src.api.episodesApi import *

async def create_episodes_db():
    all_episodes = await get_episodes_of_api()
    return all_episodes