# codging: utf-8
# This file containes your app and routes

from flask import Flask
from flask_restful import Api
from resources.ping import Ping

# APP
app = Flask(__name__)
api = Api(app)

# routes
api.add_resource(Ping, '/', '/ping')

# Running APP
if __name__ == '__main__':
  app.run(debug=True)