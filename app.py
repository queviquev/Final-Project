from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/aboutme/")
def aboutme():
    return render_template('aboutme.html')

@app.route("/hireme/")
def hireme():
    return render_template("hireme.html")

@app.route("/privacypolicy/")
def privacypolicy():
    return render_template("privacypolicy.html")