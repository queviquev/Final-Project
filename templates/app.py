import re
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def nav():
    return render_template("mytemplate.html")

@app.route("/index/")
def home():
    return render_template("index.html")

@app.route("/aboutme/")
def aboutme():
    return render_template("aboutme.html")

@app.route("/hireme/")
def hireme():
    return render_template("hireme.html")