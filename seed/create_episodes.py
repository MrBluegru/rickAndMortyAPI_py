from src.api.episodesApi import *
from config.database import get_db
from src.db.models import Episode


def create_episodes_db():
	db = get_db()
	all_episodes = get_episodes_of_api()
	episodes = []

	for episode_data in all_episodes:
			episode = Episode(
					id=episode_data['id'],
					name=episode_data['name'],
					air_date=episode_data['air_date'],
					episode=episode_data['episode']
			)
			episodes.append(episode)

	db.add_all(episodes)
	db.commit()
	db.close()
