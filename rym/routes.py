from rym import app
from flask import render_template, request, flash
from rym.models import RyMAPI
import random

rm = RyMAPI()

@app.route("/")
def index():
    random_number = random.randint(1,800)
    try:
        data = rm.oneCharacterById(random_number)
        return render_template("index.html",
                           data= data 
                           )
    except:
       flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
       return render_template("index.html", 
                              data= None)

# PERSONAJES
@app.route("/characters", 
           methods = ["GET", "POST"])
def character():
    
    if request.method == "GET":
        try:
            personaje = rm.allCharacters()
            personajes = personaje["results"]
            return render_template("characters.html",
                                title="Listado de personajes",
                                data= personajes)
        except:
            flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
            return render_template("characters.html",
                                title="Listado de personajes",
                                data= None)
    
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
    try:
        personaje = rm.oneCharacterById(id)
        return render_template("characterDetail.html",
                            title="Detalle",
                            data=personaje)
    except:
            flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
            return render_template("characterDetail.html",
                            title="Detalle",
                            data=None)

# LOCALIZACIONES
@app.route("/locations", 
           methods = ["GET", "POST"])
def location():
    if request.method == "GET":
        try:
            localizaciones= rm.allLocations()
            localizaciones = localizaciones["results"]

            return render_template("locations.html",
                                title = "Localizaciones",
                                data = localizaciones)
        except:
            flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
            return render_template("locations.html",
                                title = "Localizaciones",
                                data = None)
    else:
         if request.form["Button"] == "pagina":
            number = int(request.form["number"])
            try:
                localizaciones= rm.locationPage(number)
                localizaciones = localizaciones["results"]
                
                return render_template("locations.html",
                                    title="Localizaciones",
                                    data = localizaciones,
                                    number=number)
            except:
                flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
                return render_template("locations.html",
                                    title="Localizaciones",
                                    data = None)

#EPISODIOS
@app.route("/episodes", 
           methods = ["GET", "POST"])
def episode():
    if request.method == "GET":
        try:
            episodios = rm.allEpisodes()
            episodios = episodios["results"]
            return render_template("episodes.html",
                                title = "Episodios",
                                data = episodios)
        except:
            flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
            return render_template("episodes.html",
                                            title = "Episodios",
                                            data = None)
    else:
         if request.form["Button"] == "pagina":
            number = int(request.form["number"])
            try:
                episodios = rm.episodesPage(number)
                episodios = episodios["results"]
                
                return render_template("episodes.html",
                                    title="Episodios",
                                    data = episodios)
            except:
                flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
                return render_template("episodes.html",
                                    title="Episodios",
                                    data = None)

# BUSCADOR         
@app.route("/search", 
           methods = ["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html",
                            title = "Buscador"
                            )

    else:
         if request.form["Button3"] == "submit":
            
            nombre= request.form["search"]
            try:
                resultado = rm.charactersName(nombre)
                resultados = resultado["results"]
            
                return render_template("search.html",
                                    title="Buscador",
                                    data = resultados
                                    )
            except:
                flash("Vaya!! Algo no ha ido como debería.... intentalo de neuvo dentro de un rato...")
                return render_template("search.html",
                                    title="Buscador",
                                    data = None
                                    )