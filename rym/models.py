import requests

class RyMAPI:
    def __init__(self):
        pass

    def oneCharacterById(self, id):
        id = str(id)
        url = f"https://rickandmortyapi.com/api/character/{id}"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")

    def allCharacters(self):
        url = "https://rickandmortyapi.com/api/character"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")

    def allLocations(self):
        url="https://rickandmortyapi.com/api/location"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")

    def allEpisodes(self):
        url=" https://rickandmortyapi.com/api/episode"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")




