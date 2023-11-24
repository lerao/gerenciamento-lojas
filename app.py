from flask import Flask, request, render_template
import json

app = Flask(__name__)

from servicos import servicos_blueprint
from produtos import produtos_blueprint
from categorias import categorias_blueprint
from usuarios import usuarios_blueprint
from lojas import lojas_blueprint
from faq import faq_blueprint
from promocoes import promocoes_blueprint
from layout import layout_blueprint
from paginas import paginas_blueprint
from mailing import mailing_blueprint

@app.route("/")
def index():
  return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
  return render_template("dashboard.html")

@app.route("/logout")
def logout():
  return render_template("login.html")

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

app.register_blueprint(servicos_blueprint)
app.register_blueprint(produtos_blueprint)
app.register_blueprint(categorias_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(lojas_blueprint)
app.register_blueprint(faq_blueprint)
app.register_blueprint(promocoes_blueprint)
app.register_blueprint(layout_blueprint)
app.register_blueprint(paginas_blueprint)
app.register_blueprint(mailing_blueprint)

if __name__ == "__main__":
  app.run(debug=True, port=5001)
