from flask_restful import Resource

class Ping(Resource):

  def __init__(self):
    self.notImplemented = {
      'code': 501,
      'msg': "Not Implemented"
    }

  def get(self):
    return {
      'code': 200,
      'message': 'Pong'
    }, 200
  
  def post(self):
    return self.notImplemented, 501
  
  def put(self):
    return self.notImplemented, 501

  def delete(self):
    return self.notImplemented, 501

  def options(self):
    return self.notImplemented, 501
  
  def headers(self):
    return self.notImplemented, 501