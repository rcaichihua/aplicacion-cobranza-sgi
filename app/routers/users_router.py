from app import app, db2, api2
from flask import request
from flask_restx import Resource
from app.schemas.users_schema import UsersRequestSchema
from app.controller.users_controller import UsersController

user_ns = api2.namespace(
    name='Users',
    description='Users routers',
    path='/users'
)

request_schema = UsersRequestSchema(user_ns)


@user_ns.route('/')
class Users(Resource):
    def get(self):
        """List all Users"""
        controller = UsersController()
        return controller.all()

    @api2.expect(request_schema.create(), validate=True)
    def post(self):
        """ Create new Rol """
        controller = UsersController()
        return controller.create(request.json)


@user_ns.route('/<int:id>')
class UserById(Resource):
    def get(self, id):
        """List User by Id"""
        controller = UsersController()
        return controller.get_by_id(id)

    @api2.expect(request_schema.update(), validate=True)
    def put(self, id):
        """Update User by Id"""
        controller = UsersController()
        return controller.update(id, request.json)

    def delete(self, id):
        """Deleted User by Id"""
        controller = UsersController()
        return controller.delete(id)


api2.add_namespace(user_ns)
