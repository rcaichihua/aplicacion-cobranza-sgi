from lib2to3.pytree import Base
from flask import request
import restx
from app import app, db2
from app import routers
#from app import models

from app.models.base import BaseModel
BaseModel.set_session(db2.session)

users = [
    {
        "id": 1,
        "names": "Roger"
    }
]


@app.route('/', methods=['GET'])
def index():
    return {
        'message': 'Hello World'
    }


@app.route('/users', methods=['GET'])
def user_list():
    return users, 201


@app.route('/users/<int:id>', methods=['GET'])
def user_get_by_id(id):
    for user in users:
        if user['id'] == id:
            return user, 200
    return {
               'message': 'User does not exist'
           }, 404


@app.route('/users', methods=['POST'])
def user_create():
    body = request.get_json()
    users.append(body)
    return {
               'message': 'User created successfully'
           }, 201


@app.route('/users/<int:id>', methods=['PUT'])
def user_update(id):
    body = request.get_json()

    for user in users:
        if user['id'] == id:
            user['nombres'] = body['nombres']
            return {
                       'message': 'User updated'
                   }, 200
    return {
               'message': 'Usuario ingresado no existe'
           }, 404


@app.route('/users/<int:id>', methods=['DELETE'])
def user_delete(id):
    for index, value in enumerate(users):
        if value['id'] == id:
            users.pop(index)
            return {
                       'message': 'Eliminado correctamente'
                   }, 200
    return {
               'message': 'Not found'
           }, 404
