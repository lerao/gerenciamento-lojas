
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

paginas_blueprint = Blueprint('paginas', __name__)

@paginas_blueprint.route("/paginas")
def paginas():
  return render_template("dashboard.html")
