from flask_restx import fields
from marshmallow import fields as field
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.roles_model import RoleModel


class RolesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, min_length=2, max_length=50)
        })

    def update(self):
        return self.namespace.model('Role Update', {
            'name': fields.String(required=True, min_length=2, max_length=50)
        })


class RolesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
        ordered = True

    users = field.List(field.Nested('UsersResponseSchema', exclude=("role",)))

# Documentation https://marshmallow.readthedocs.io/en/stable/nesting.html#nesting-a-schema-within-itself
# maximum recursion depth exceeded while calling a python object
