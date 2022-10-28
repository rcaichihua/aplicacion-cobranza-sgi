from app import api2
from flask import request
from flask_restx import Resource
from app.schemas.auth_schema import AuthRequestSchema
from app.controller.auth_controller import AuthController
from flask_jwt_extended import jwt_required, get_jwt_identity

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

@auth_ns.route('/token/refresh')
class TokenRefresh(Resource):
    @auth_ns.expect(request_schema.refresh_token())
    @jwt_required(refresh=True)
    def post(self):
        """Get new access toke from refresh token"""
        identity = get_jwt_identity()
        controller = AuthController()
        return controller.refresh_token(identity)

api2.add_namespace(auth_ns)
