# encoding: utf-8
# file: api/errors/handler.py

from api.run import app
from flask import json
from werkzeug.exceptions import HTTPException

"""
  Handler errors
"""
@app.errorhandler(HTTPException)
def handlerException(error):
  """
    Return JSON instead of HTML for HTTP errors.
  """
  response = error.get_response()
  response.data = json.dumps({
    "code": error.code,
    "name": error.name,
    "description": error.description
  })
  response.content_type = "application/json"
  return response