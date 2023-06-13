from rym import app
from flask import render_template
from rym.models import RyMAPI
import random

rm = RyMAPI()

@app.route("/")
def index():
    random_number = random.randint(1,800)
    
    return render_template("index.html", 
                           number=random_number)

@app.route("/characters")
def character():
    personaje = rm.allCharacters()
    personajes = personaje["results"]

    return render_template("characters.html",
                           title="Listado de personajes",
                           data= personajes)

@app.route("/locations")
def location():
    return render_template("locations.html",
                           title = "Localizaciones")

@app.route("/episodes")
def episode():
    return render_template("episodes.html",
                           title = "Episodios")