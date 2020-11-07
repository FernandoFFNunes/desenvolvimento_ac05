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
def pontuacao():
    return render_template("pontuacao")

@app.route("/times")
def times():
    return render_template("times")

@app.route("/jogadores")
def jogadores():
    return render_template("jogadores")
