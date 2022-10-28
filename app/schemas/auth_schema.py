from flask_restx import fields
from flask_restx.reqparse import RequestParser


class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def sign_in(self):
        return self.namespace.model('Auth SignIn', {
            'user_name': fields.String(required=True),
            'password': fields.String(required=True)
        })

    def reset_password(self):
        return self.namespace.model('Auth Reset Password',{
            'email': fields.String(required=True)
        })

    def refresh_token(self):
        parser = RequestParser()
        parser.add_argument(
            'Authorization',
            type=str,
            location='headers',
            help='Example: Bearer (Refresh_token)'
        )
        return parser
