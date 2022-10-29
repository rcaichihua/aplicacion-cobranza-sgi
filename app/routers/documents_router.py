from app import app, db2, api2
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.documents_schema import DocumentsRequestSchema
from app.controller.documents_controller import DocumentsController

document_ns = api2.namespace(
    name='Documents',
    description='Documents routers',
    path='/documents'
)

request_schema = DocumentsRequestSchema(document_ns)


@document_ns.route('/')
@document_ns.doc(security='Bearer')
class Documents(Resource):
    @jwt_required()
    @document_ns.expect(request_schema.all())
    def get(self):
        """List all Documents"""
        query_params = request_schema.all().parse_args()
        controller = DocumentsController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @api2.expect(request_schema.create(), validate=True)
    def post(self):
        """ Create new Document """
        print('hola')
        controller = DocumentsController()
        print('request.json')
        return controller.create(request.json)


@document_ns.route('/<int:id>')
@document_ns.doc(security='Bearer')
class DocumentById(Resource):
    @jwt_required()
    def get(self, id):
        """List Document by Id"""
        controller = DocumentsController()
        return controller.get_by_id(id)

    @jwt_required()
    @api2.expect(request_schema.update(), validate=True)
    def put(self, id):
        """Update Document by Id"""
        controller = DocumentsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        """Disabled Document by Id"""
        controller = DocumentsController()
        return controller.delete(id)


api2.add_namespace(document_ns)
