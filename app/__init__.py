# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
#app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')
username = urllib.parse.quote_plus('babs')
password = urllib.parse.quote_plus('babs123')
client = MongoClient('mongodb://%s:%s@localhost' % (username, password))
db = client['addedDB']

# bs = Bootstrap(app) #flask-bootstrap
# db = SQLAlchemy(app) #flask-sqlalchemy

# lm = LoginManager()
# lm.setup_app(app)
# lm.login_view = 'login'

from app import views