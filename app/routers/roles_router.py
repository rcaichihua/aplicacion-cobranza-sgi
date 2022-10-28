from app import app, db2, api2
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controller.roles_controller import RolesController
from flask_jwt_extended import jwt_required

role_ns = api2.namespace(
    name='Roles',
    description='Role routers',
    path='/roles'
)

request_schema = RolesRequestSchema(role_ns)


@role_ns.route('/')
@role_ns.doc(security='Bearer')
class Role(Resource):
    @jwt_required()
    def get(self):
        """List all Roles"""
        controller = RolesController()
        return controller.all()

    @jwt_required()
    @api2.expect(request_schema.create(), validate=True)
    def post(self):
        """ Create new Rol """
        controller = RolesController()
        return controller.create(request.json)


@role_ns.route('/<int:id>')
@role_ns.doc(security='Bearer')
class RoleById(Resource):
    @jwt_required()
    def get(self, id):
        """List Roles by Id"""
        controller = RolesController()
        return controller.get_by_id(id)

    @jwt_required()
    @api2.expect(request_schema.update(), validate=True)
    def put(self, id):
        """Update role by Id"""
        controller = RolesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        """Deleted role by Id"""
        controller = RolesController()
        return controller.delete(id)


api2.add_namespace(role_ns)
