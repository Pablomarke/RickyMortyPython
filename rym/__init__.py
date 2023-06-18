from flask import Flask

app = Flask(__name__)

#key necesaria para funcionamiento
app.secret_key = "b'_5#y2"

from rym.routes import *