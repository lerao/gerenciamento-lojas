
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import requests

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pagina.db'  # Configuração para usar SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita avisos desnecessários
db = SQLAlchemy(app)

paginas_blueprint = Blueprint('paginas', __name__)

@paginas_blueprint.route("/paginas")
def paginas():
  return render_template("paginas.html")

paginas_blueprint = Blueprint('paginas', __name__)
@paginas_blueprint.route("/paginas")
def paginas():

  backend_url = 'http://127.0.0.1:5000/paginas'
  response = requests.get(backend_url)

  if response.status_code == 200:
      paginas = response.json()
      return render_template('paginas.html', dados=paginas, pagina=(0,0))
  else:
    return render_template("paginas.html", dados=[], pagina=(0,0))
 
@paginas_blueprint.route("/paginas/delete/<id>")
def paginaDelete(id):
  bd = db.SQLiteConnection('Pagina.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM paginas WHERE id = {id}")
  return redirect(url_for('paginas'))

@paginas_blueprint.route("/paginas/edit/<id>")
def paginaEdit(id):
  bd = db.SQLiteConnection('Pagina.db')
  bd.connect()
  query = f"select id, nome from paginas where id = {id};"
  nome = bd.execute_query(query)
  return render_template("paginas.html", pagina=nome)
