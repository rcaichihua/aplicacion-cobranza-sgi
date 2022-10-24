from app import app, db2, api2
from flask_restx import Resource

user_ns = api2.namespace(
    name='Users',
    description='Users routers',
    path='/users'
)


@user_ns.route('/')
class Users(Resource):
    def get(self):
        return {
            'message': 'List users'
        }

    def post(self):
        return {
            'message': 'Request Body'
        }


@user_ns.route('/<int:id>')
class UserById(Resource):
    def get(self, id):
        return {
            'message': f'List users for id {id}'
        }

    def put(self, id):
        return {
            'message': f'update for id {id}'
        }

    def delete(self, id):
        return {
            'message': f'Delete users id {id}'
        }