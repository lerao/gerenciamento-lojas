
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

servicos_blueprint = Blueprint('servicos', __name__)

@servicos_blueprint.route("/servicos")
def servicos():
  return render_template("dashboard.html")
