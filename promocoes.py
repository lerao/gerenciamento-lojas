
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import requests

promocoes_blueprint = Blueprint('promocoes', __name__)


@promocoes_blueprint.route("/promocoes")
def promocoes():

  backend_url = 'http://127.0.0.1:5000/promocoes'
  response = requests.get(backend_url)

  if response.status_code == 200:
      promocoes = response.json()
      return render_template('promocoes.html', dados=promocoes, promocao=(0,0))
  else:
    return render_template("promocoes.html", dados=[], promocao=(0,0))
  
@promocoes_blueprint.route("/promocoes/delete/<id>")
def promocaoDelete(id):
  bd = db.SQLiteConnection('Promocao.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM promocoes WHERE id = {id}")
  return redirect(url_for('promocoes'))

@promocoes_blueprint.route("/promocoes/edit/<id>")
def promocoesEdit(id):
  bd = db.SQLiteConnection('Promocao.db')
  bd.connect()
  query = f"select id, nome from promocoes where id = {id};"
  nome = bd.execute_query(query)
  return render_template("promocoes.html", promocao=nome)
