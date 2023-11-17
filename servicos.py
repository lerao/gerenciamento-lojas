
from flask import Flask, render_template, request, redirect, Blueprint

servicos_blueprint = Blueprint('servicos', __name__)

@servicos_blueprint.route("/servicos")
def servicos():
  return render_template("servicos.html")
