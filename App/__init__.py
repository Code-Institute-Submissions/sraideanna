""" Internal module imports """

import os

""" External module imports """

from flask import Flask     
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_mail import Mail

""" Initiate flask app """

app = Flask(__name__)

""" Environment variables """

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

""" Activate mongodb"""

mongo = PyMongo(app)
db = mongo.db
login_manager = LoginManager(app)

""" Tell flask-login where the login page is, and set the alert message """

login_manager.login_view = 'login'
login_manager.login_message = u"You must be logged in to visit this page."
login_manager.login_message_category = 'info'

""" Activate mail module for the reset password email """

mail = Mail(app)

""" Import routes (after app configuration to avoid import inconsistencies) """

from App import routes

