
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import flask_cors
import requests

faq_blueprint = Blueprint('faq', __name__)


@faq_blueprint.route("/faq")
def faq():

  backend_url = 'http://127.0.0.1:5000/faq'
  response = requests.get(backend_url)

  if response.status_code == 200:
      faqs = response.json()
      return render_template('faq.html', dados=faqs, faq=(0,0))
  else:
    return render_template("faq.html", dados=[], faq=(0,0))
  
@faq_blueprint.route("/faq/delete/<id>")
def faqDelete(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM faq WHERE id = {id}")
  return redirect(url_for('faq'))

@faq_blueprint.route("/faq/edit/<id>")
def faqEdit(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  query = f"select id, nome from faq where id = {id};"
  nome = bd.execute_query(query)
  return render_template("faq.html", faq=nome)
