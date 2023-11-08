
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import database as db

categorias_blueprint = Blueprint('categorias', __name__)


@categorias_blueprint.route("/categorias-")
def categorias():
  bd = db.SQLiteConnection('estoque.db')
  bd.connect()
  categorias = bd.execute_query("select * from categorias;")
  print(categorias)
  return render_template("categorias.html", dados=categorias, categoria=(0,0))

@categorias_blueprint.route("/categoria/save", methods=["POST"])
def categoriaSave():
  nome = request.form['nomeCategoria']
  id = request.form['id']
  bd = db.SQLiteConnection('estoque.db')
  bd.connect()
  if id:
    query = f"UPDATE categorias SET nome ='{nome}' WHERE id = {id}"
  else:
    query = f"INSERT INTO categorias (nome) VALUES ('{nome}')"
  print(query)
  bd.execute_query(query)
  return redirect(url_for('categorias'))
  
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
