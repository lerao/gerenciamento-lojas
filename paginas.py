
from flask import Flask, render_template, request, redirect, Blueprint

paginas_blueprint = Blueprint('paginas', __name__)

@paginas_blueprint.route("/paginas")
def paginas():
  return render_template("paginas.html")
