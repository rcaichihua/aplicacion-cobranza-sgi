from flask_restx import fields
from marshmallow import fields as field
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.documents_model import DocumentModel
from flask_restx.reqparse import RequestParser
from datetime import time

# Request the data from the front - what the front sends - validates the fields that are received
class DocumentsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Documents Create', {
            'type_doc': fields.String(required=True, max_length=2, nullable=False),
            'series': fields.String(required=True, min_length=4, max_length=4, nullable=False),
            'number': fields.String(required=True, min_length=8, max_length=8, nullable=False),
            'issue_date': fields.String(required=True, description='Date in D/M/Y Example 06/12/2022'),
            'collect_date': fields.String(required=True, description='Date in D/M/Y Example 06/12/2022'),
            'amount': fields.String(required=True),
            #'status': fields.String(required=True, min_length=1, max_length=1, nullable=False, default='P'),
            'user_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Document Update', {
            'type_doc': fields.String(required=False, max_length=2, nullable=False),
            'series': fields.String(required=False, min_length=4, max_length=4, nullable=False),
            'number': fields.String(required=False, min_length=8, max_length=8, nullable=False),
            'issue_date': fields.String(required=False, description='Date in D/M/Y Example 06/12/2022'),
            'collect_date': fields.String(required=False, description='Date in D/M/Y Example 06/12/2022'),
            #'process_date': fields.DateTime(dt_format="iso8601", year=2020),
            'amount': fields.String(required=False),
            'status': fields.String(required=True, min_length=1, max_length=1, nullable=False, default='P', description='P: Pendiente, A: Anulado, C: Cancelado'),
            'user_id': fields.Integer(required=False)
        })


# What the service responds - here is the serializer - returns the objects
class DocumentsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentModel
        ordered = True
        # include_fk = True -> use relationship in user model y rol model
    user = field.Nested('UsersResponseSchema', only=("id", "name"), many=False)
