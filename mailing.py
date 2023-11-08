
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

mailing_blueprint = Blueprint('mailing', __name__)

@mailing_blueprint.route("/mailing")
def mailing():
  return render_template("dashboard.html")
