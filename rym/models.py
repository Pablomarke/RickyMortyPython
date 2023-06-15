import requests

class RyMAPI:
    def __init__(self):
        pass

# FUNCION PARA OBTENER UN PERSONAJE MEDIANTE ID
    def oneCharacterById(self, id):
        id = str(id)
        url = f"https://rickandmortyapi.com/api/character/{id}"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")

# FUNCIÓN PARA CONSEGUIR TODOS LOS PERSONAJES
    def allCharacters(self):
        url = "https://rickandmortyapi.com/api/character"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")
# FUNCIÓN PARA CONSEGUIR TODOS LOS PERSONAJES en PAGINAS
    def charactersPage(self, number):
       url = f"https://rickandmortyapi.com/api/character/?page={number}"
       response = requests.get(url)
       r = response.json()
       if response.status_code == 200:
            return r
       else:
            print("NO")

# FUNCION PARA CONSEGUIR TODAS LAS LOCALIZACIONES
    def allLocations(self):
        url="https://rickandmortyapi.com/api/location"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")

# FUNCION PARA CONSEGUIR TODAS LAS LOCALIZACIONES en PAGINAS
    def locationPage(self, number):
       url = f"https://rickandmortyapi.com/api/location/?page={number}"
       response = requests.get(url)
       r = response.json()
       if response.status_code == 200:
            return r
       else:
            print("NO")

# FUNCION PARA CONSEGUIR TODOS LOS EPISODIOS
    def allEpisodes(self):
        url=" https://rickandmortyapi.com/api/episode"
        response = requests.get(url)
        r = response.json()
        if response.status_code == 200:
            return r
        else:
            print("NO")

# FUNCION PARA CONSEGUIR TODOS LOS EPISODIOS en PAGINAS
    def episodesPage(self, number):
       url = f"https://rickandmortyapi.com/api/episode/?page={number}"
       response = requests.get(url)
       r = response.json()
       if response.status_code == 200:
            return r
       else:
            print("NO")




