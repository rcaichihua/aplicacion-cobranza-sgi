from flask_restx import fields
from marshmallow import fields as field
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.users_model import UserModel
from flask_restx.reqparse import RequestParser


# Request the data from the front - what the front sends - validates the fields that are received
class UsersRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('User Create', {
            'code_debd_collector': fields.String(required=False, max_length=20, nullable=True),
            'name': fields.String(required=True, min_length=2, max_length=50, nullable=False),
            'last_name': fields.String(required=True, min_length=2, max_length=50, nullable=False),
            'user_name': fields.String(required=True, min_length=2, max_length=50, unique=True, nullable=False),
            'password': fields.String(required=True, min_length=5, max_length=200, nullable=False),
            'email': fields.String(required=True, min_length=10, max_length=50, unique=True),
            'rol_id': fields.Integer(readonly=True, default=2)
        })

    def update(self):
        return self.namespace.model('User Update', {
            'code_debd_collector': fields.String(required=False, max_length=20),
            'name': fields.String(required=False, min_length=2, max_length=50, nullable=False),
            'last_name': fields.String(required=False, min_length=2, max_length=50, nullable=False),
            'user_name': fields.String(required=False, min_length=2, max_length=50, unique=True, nullable=False),
            'password': fields.String(required=False, min_length=5, max_length=200, nullable=False),
            'email': fields.String(required=False, min_length=10, max_length=50, unique=True)
        })


# What the service responds - here is the serializer - returns the objects
class UsersResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True
        # include_fk = True -> use relationship in user model y rol model
    role = field.Nested('RolesResponseSchema', only=("id", "name"), many=False)


# Documentation https://marshmallow.readthedocs.io/en/stable/nesting.html#nesting-a-schema-within-itself
# maximum recursion depth exceeded while calling a python object
