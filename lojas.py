
from flask import Flask, render_template, request, redirect, Blueprint

lojas_blueprint = Blueprint('lojas', __name__)

@lojas_blueprint.route("/lojas")
def lojas():
  return render_template("empresa.html")
