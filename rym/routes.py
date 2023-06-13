from rym import app
from flask import render_template
from rym.models import RyMAPI

rm = RyMAPI()

@app.route("/")
def index():
    
    return render_template("index.html", 
                           title="Inicio")

@app.route("/characters")
def character():
    personaje = rm.allCharacters()
    personajes = personaje["results"]
    """nombre = personaje["name"]
    estado = personaje["status"]
    especie = personaje["species"]
    genero = personaje["gender"]
    datos = [nombre, estado, especie,genero]"""

    return render_template("characters.html",
                           title="Listado de personajes",
                           data= personajes)