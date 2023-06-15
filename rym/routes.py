from rym import app
from flask import render_template, request
from rym.models import RyMAPI
import random

rm = RyMAPI()


@app.route("/")
def index():
    random_number = random.randint(1,800)
    data = rm.oneCharacterById(random_number)
    return render_template("index.html",
                           data= data 
                           )

# PERSONAJES
@app.route("/characters", 
           methods = ["GET", "POST"])
def character():
    
    if request.method == "GET":
        personaje = rm.allCharacters()
        personajes = personaje["results"]
        
        return render_template("characters.html",
                            title="Listado de personajes",
                            data= personajes)
    
    else: 
        if request.form["Button"] == "pagina":
            number = int(request.form["number"])
            personajes = rm.charactersPage(number)
            personajes = personajes["results"]
            
            return render_template("characters.html",
                                title="Listado de personajes",
                                data = personajes,
                                number=number)

@app.route("/characterdetailed<int:id>")
def characterdetail(id):
    personaje = rm.oneCharacterById(id)
    
    return render_template("characterDetail.html",
                           title="Detalle",
                           data=personaje)

# LOCALIZACIONES
@app.route("/locations", 
           methods = ["GET", "POST"])
def location():
    if request.method == "GET":
        localizaciones= rm.allLocations()
        localizaciones = localizaciones["results"]

        return render_template("locations.html",
                            title = "Localizaciones",
                            data = localizaciones)
    else:
         if request.form["Button"] == "pagina":
            number = int(request.form["number"])
            localizaciones= rm.locationPage(number)
            localizaciones = localizaciones["results"]
            
            return render_template("locations.html",
                                title="Localizaciones",
                                data = localizaciones,
                                number=number)

#EPISODIOS
@app.route("/episodes", 
           methods = ["GET", "POST"])
def episode():
    if request.method == "GET":
        episodios = rm.allEpisodes()
        episodios = episodios["results"]
        return render_template("episodes.html",
                            title = "Episodios",
                            data = episodios)

    else:
         if request.form["Button"] == "pagina":
            number = int(request.form["number"])
            episodios = rm.episodesPage(number)
            episodios = episodios["results"]
            
            return render_template("episodes.html",
                                title="Episodios",
                                data = episodios,
                                number=number)