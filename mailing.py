
from flask import Flask, render_template, request, redirect, Blueprint

mailing_blueprint = Blueprint('mailing', __name__)

@mailing_blueprint.route("/mailing")
def mailing():
  return render_template("mailing.html")
