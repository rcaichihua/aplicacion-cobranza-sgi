from app import api2
from flask import request
from flask_restx import Resource
from app.schemas.auth_schema import AuthRequestSchema
from app.controller.auth_controller import AuthController

auth_ns = api2.namespace(
    name='Authentication',
    description='Authentication module path',
    path='/auth'
)

request_schema = AuthRequestSchema(auth_ns)


@auth_ns.route('/signin')
class SignIn(Resource):
    @api2.expect(request_schema.sign_in(), validate=True)
    def post(self):
        """ create authentication token """
        controller = AuthController()
        return controller.sign_in(request.json)


api2.add_namespace(auth_ns)
