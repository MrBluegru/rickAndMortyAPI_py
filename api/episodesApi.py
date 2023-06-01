import requests


def get_episodes_of_api():
    base_url = "https://rickandmortyapi.com/api/episode?page={}"
    num_urls = 42
    urls = [base_url.format(i) for i in range(1, num_urls+1)]
    all_episodes = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["results"]
            all_episodes.extend(data)

    mapped_data = []
    for episode in all_episodes:
        characters = [char.split("/")[-1] for char in episode["characters"]]

    mapped_data = list(map(lambda episode: {
        "id": episode["id"],
        "name": episode["name"],
        "air_date": episode["air_date"],
        "episode": episode["episode"],
        "characters": characters,
    }, all_episodes))

    return mapped_data
