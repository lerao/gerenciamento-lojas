
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import requests

categorias_blueprint = Blueprint('categorias', __name__)


@categorias_blueprint.route("/categorias")
def categorias():

  backend_url = 'http://127.0.0.1:5000/categoria'
  response = requests.get(backend_url)

  if response.status_code == 200:
      categorias = response.json()
      return render_template('categorias.html', dados=categorias, categoria=(0,0))
  else:
    return render_template("categorias.html", dados=[], categoria=(0,0))
  
@categorias_blueprint.route("/categoria/delete/<id>")
def categoriaDelete(id):
  bd = db.SQLiteConnection('estoque.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM categorias WHERE id = {id}")
  return redirect(url_for('categorias'))

@categorias_blueprint.route("/categoria/edit/<id>")
def categoriaEdit(id):
  bd = db.SQLiteConnection('estoque.db')
  bd.connect()
  query = f"select id, nome from categorias where id = {id};"
  nome = bd.execute_query(query)
  return render_template("categorias.html", categoria=nome)
