from flask import Flask
from flask import render_template
from templates.socials import get_social

app = Flask(__name__)

import os

catfolder = os.path.join('static', 'cats')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = catfolder

@app.route("/")
def home():
    social = get_social()
    return render_template("index.html", social=social)

@app.route("/portfolio")
def portfolio():
    social = get_social()
    return render_template('portfolio.html', social=social)

@app.route("/aboutme/")
def aboutme():
    cat1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ozzyfunnyzzz.jpg')
    catList = os.listdir('static/cats')
    catList = ['cats/' + image for image in catList]
    social = get_social()
    return render_template('aboutme.html', social=social, catList=catList)

@app.route("/hireme/")
def hireme():
    social = get_social()
    return render_template("hireme.html", social=social)

@app.route("/privacypolicy/")
def privacypolicy():
    social = get_social()
    return render_template("privacypolicy.html", social=social)

if __name__ == '__main__':
    app.run(debug=True)