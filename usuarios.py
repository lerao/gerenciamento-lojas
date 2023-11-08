
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

usuarios_blueprint = Blueprint('usuarios', __name__)

@usuarios_blueprint.route("/usuarios")
def usuarios():
  return render_template("dashboard.html")
