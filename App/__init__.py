""" External module imports """
from flask import Flask, render_template
from flask_pymongo import PyMongo
""" Internal module imports """
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')