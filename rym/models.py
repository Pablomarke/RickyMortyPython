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
            print(r)
        else:
            print("NO")


