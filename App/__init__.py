""" External module imports """
from flask import Flask     
from flask_pymongo import PyMongo
""" Internal module imports """
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

# mongo = PyMongo(app)
# db = mongo.db


from App import routes

