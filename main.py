from crypt import methods
from flask import Flask, request

app = Flask(__name__)

users = [
  {
    "id":1,
    "nombres":"Roger"
  }
]

@app.route('/', methods=['GET'])
def index():
  return {
    'message':'Hello World'
  }

@app.route('/users', methods=['GET'])
def userList():
  return users, 201

@app.route('/users/<int:id>', methods=['GET'])
def userGetById(id):
  for user in users:
    if user['id']==id:
      return user, 200
  return {
    'message':'Usuario ingresado no existe'
  }, 404

@app.route('/users', methods=['POST'])
def userCreate():
  body = request.get_json()
  users.append(body)
  return {
    'message':'Usuario creado correctamente'
  }, 201

@app.route('/users/<int:id>', methods=['PUT'])
def userUpdate(id):
  body = request.get_json()

  for user in users:
    if user['id'] == id:
      user['nombres'] = body['nombres']
      return {
        'messager': 'USuario actualizado'
      }, 200
  return {
    'message':'Usuario ingresado no existe'
  }, 404 

@app.route('/users/<int:id>', methods=['DELETE'])
def userDelete(id):
  for index, value in enumerate(users):
    if value['id']==id:
      users.pop(index)
      return {
        'message':'Eliminado correctamente'
      }, 200
  return {
    'message':'No encontrado'
  }, 404
    