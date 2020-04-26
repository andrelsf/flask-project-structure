# codging: utf-8
# This file containes your app and routes

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# APP
app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('./utils/config.py')

# SQLAlchemy
db = SQLAlchemy(app)

# Import Resources
from api.resources.ping import Ping

# routes
api.add_resource( Ping, '/', '/ping')
