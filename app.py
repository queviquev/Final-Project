from flask import Flask
from flask import render_template
from socials import get_social
import os

app = Flask(__name__)

social = get_social()

catfolder = os.path.join('static', 'cats')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = catfolder

@app.route("/")
def home():
    return render_template("index.html", social)

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', social)

@app.route("/aboutme/")
def aboutme():
    cat1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ozzyfunnyzzz.jpg')
    catList = os.listdir('static/cats')
    catList = ['cats/' + image for image in catList]
    return render_template('aboutme.html', social, catList=catList)

@app.route("/hireme/")
def hireme():
    return render_template("hireme.html", social)

@app.route("/privacypolicy/")
def privacypolicy():
    return render_template("privacypolicy.html", social=social)

if __name__ == '__main__':
    app.run(debug=True)