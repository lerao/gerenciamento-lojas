from flask import Flask, request, render_template
import json
import database as db

app = Flask(__name__)

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

@app.route("/categorias")
def categorias():
  bd = db.SQLiteConnection('storemanager.db')
  bd.connect()
  categorias = bd.execute_query("select * from categorias;")
  return render_template("categorias.html", dados=categorias)

@app.route("/setup")
def setup():
  bd = db.SQLiteConnection('storemanager.db')
  bd.connect()
  bd.create_database()
  bd.execute_query("TRUNCATE TABLE categorias;")
  bd.execute_query("INSERT INTO categorias VALUES (1, 'Carnes');")
  bd.execute_query("INSERT INTO categorias VALUES (2, 'Gelados');")
  return "Instalado com sucesso!"

if __name__ == "__main__":
  app.run(debug=True)
