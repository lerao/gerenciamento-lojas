
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

layout_blueprint = Blueprint('layout', __name__)

@layout_blueprint.route("/layout")
def layout():
  return render_template("layout.html")
