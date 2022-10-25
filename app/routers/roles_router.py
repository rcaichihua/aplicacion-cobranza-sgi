from app import app, db2, api2
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controller.roles_controller import RolesController

role_ns = api2.namespace(
    name='Roles',
    description='Role routers',
    path='/roles'
)

request_schema = RolesRequestSchema(role_ns)


@role_ns.route('/')
class Role(Resource):
    def get(self):
        """List all Roles"""
        controller = RolesController()
        return controller.all()

    @api2.expect(request_schema.create(), validate=True)
    def post(self):
        """ Create new Rol """
        controller = RolesController()
        return controller.create(request.json)


@role_ns.route('/<int:id>')
class RoleById(Resource):
    def get(self, id):
        """List Roles by Id"""
        controller = RolesController()
        return controller.get_by_id(id)

    @api2.expect(request_schema.update(), validate=True)
    def put(self, id):
        """Update role by Id"""
        controller = RolesController()
        return controller.update(id, request.json)

    def delete(self, id):
        """Deleted role by Id"""
        controller = RolesController()
        return controller.delete(id)


api2.add_namespace(role_ns)
