from config.database import get_db
from models import character
from api.charactersApi import get_characters_of_api


async def create_characters_from_api() -> None:
	db = get_db()
	num_characters = db.query(character).count()

	if num_characters == 0:
			characters = []
			all_characters = await get_characters_of_api()
			for character_data in all_characters:
					character = character(
							id=character_data['id'],
							name=character_data['name'],
							status=character_data['status'],
							species=character_data['species'],
							gender=character_data['gender'],
							origin=character_data['origin'],
							location=character_data['location'],
							image=character_data['image']
					)
					characters.append(character)
			db.add_all(characters)
			db.commit()

	db.close()
