from flask import Flask, render_template, request, redirect, Blueprint, url_for
import requests

servicos_blueprint = Blueprint('servicos', __name__)


@servicos_blueprint.route("/servicos", methods=['GET'])
def get_servicos():
    # Substitua a URL do backend pelos serviços específicos
    backend_url = 'http://127.0.0.1:5000/servicos'
    response = requests.get(backend_url)

    if response.status_code == 200:
        servicos = response.json()
        return render_template('servicos.html', dados=servicos, servico=(0, 0))
    else:
        return render_template("servicos.html", dados=[], servico=(0, 0))

@servicos_blueprint.route("/servico/delete/<id>")
def delete_servico(id):
    bd = db.SQLiteConnection('dados.db')
    bd.connect()
    bd.execute_query(f"DELETE FROM servicos WHERE id = {id}")

@servicos_blueprint.route("/servico/edit/<id>")
def edit_servico(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  query = f"select id, nome from categorias where id = {id};"
  nome = bd.execute_query(query)
  return render_template("categorias.html", categoria=nome)


@servicos_blueprint.route("/servico/create", methods=['POST'])
def create_servico():
    # Substitua a lógica de criação de serviços conforme necessário
    backend_url = 'http://127.0.0.1:5000/criar_servicos'
    dados_novos = request.form.to_dict()
    response = requests.post(backend_url, json=dados_novos)

    if response.status_code == 201:
        return redirect(url_for('servicos.get_servicos'))
    else:
        return render_template("error.html", message="Erro ao criar o serviço")
