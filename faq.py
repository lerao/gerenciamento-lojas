
from flask import Flask, render_template, request, redirect, Blueprint
import database as db

faq_blueprint = Blueprint('faq', __name__)

@faq_blueprint.route("/faq")
def faq():
  return render_template("dashboard.html")
