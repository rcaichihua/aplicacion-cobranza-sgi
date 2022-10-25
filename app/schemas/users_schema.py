from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.users_model import UserModel


#Solicitar al front los datos - lo que el front envia - valida los campos que se recive
class UsersRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('User Create', {
            'code_debd_collector': fields.String(required=False, max_length=20, nullable=True),
            'name': fields.String(required=True, min_length=2, max_length=120, nullable=False),
            'last_name': fields.String(required=True, min_length=2, max_length=160, nullable=False),
            'user_name': fields.String(required=True, min_length=2, max_length=80, unique=True, nullable=False),
            'password': fields.String(required=True, min_length=5, max_length=200, nullable=False),
            'email': fields.String(required=True, min_length=4, max_length=50, unique=True),
            'rol_id': fields.Integer(readonly=True, default=2)
        })

    def update(self):
        return self.namespace.model('User Update', {
            'code_debd_collector': fields.String(required=False, max_length=20),
            'name': fields.String(required=False, min_length=2, max_length=120),
            'last_name': fields.String(required=False, min_length=2, max_length=160),
            'user_name': fields.String(required=False, min_length=2, max_length=80, unique=True),
            'password': fields.String(required=False, min_length=2, max_length=200, nullable=False),
            'email': fields.String(required=False, min_length=2, max_length=50, unique=True)
        })


#Lo que responde el servicio - aqui esta el serialziador - devuelve los objetos
class UsersResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True
