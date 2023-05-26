import requests

def get_characters_of_api():
    base_url = "https://rickandmortyapi.com/api/character?page={}"
    num_urls = 42
    urls = [base_url.format(i) for i in range(1, num_urls+1)]
    all_characters = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()["results"]
            all_characters.extend(data)
            
    mapped_data = list(map(lambda character: {
        "name": character["name"],
        "status": character["status"],
        "species": character["species"],
        "gender": character["gender"],
        "origin": character["origin"]["name"],
        "location": character["location"]["name"],
        "image": character["image"],
    }, all_characters))

    return mapped_data
