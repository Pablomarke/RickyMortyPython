from rym import app
from flask import render_template
from rym.models import RyMAPI

rm = RyMAPI()

@app.route("/")
def index():
    
    return render_template("index.html", 
                           title="Inicio")

@app.route("/character")
def character():
    rm.oneCharacterById(2)

    return render_template("character.html",
                           title="Personaje")