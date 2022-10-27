from flask_restx import fields


class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def sign_in(self):
        return self.namespace.model('Auth SignIn', {
            'user_name': fields.String(required=True),
            'password': fields.String(required=True)
        })
