""" Internal module imports """
import os
""" External module imports """
from flask import Flask     
from flask_pymongo import PyMongo
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
db = mongo.db
login_manager = LoginManager(app)


from App import routes

