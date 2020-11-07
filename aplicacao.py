from flask import Flask
from flask import render_template, request, url_for, redirect


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias")

@app.route("/pontuacao")
def 