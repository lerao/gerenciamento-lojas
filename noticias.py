
from flask import Flask, render_template, request, Blueprint

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import requests

noticias_blueprint = Blueprint('noticias', __name__)


@noticias_blueprint.route("/noticias")
def noticias():

  backend_url = 'http://127.0.0.1:5000/noticias'
  response = requests.get(backend_url)

  if response.status_code == 200:
      noticias = response.json()
      return render_template('noticias.html', dados=noticias, noticia=(0,0))
  else:
    return render_template("noticias.html", dados=[], noticia=(0,0))
