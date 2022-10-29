from decimal import Decimal
from app import db2
from app.models.documents_model import DocumentModel
from app.schemas.documents_schema import DocumentsResponseSchema
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


class DocumentsController:
    def __init__(self):
        self.model = DocumentModel
        self.schema = DocumentsResponseSchema

    def all(self, page, per_page):
        try:
            records = self.model.where(status='P').order_by('id').paginate(
                per_page=per_page, page=page
            )
            response = self.schema(many=True)
            #for page_num in records.items:
            #    print(page_num.collect_date)
            #print(json.dumps(response.dump(records.items), cls=JSONEncoder))
            return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def get_by_id(self, id):
        try:
            if record := self.model.where(id=id).first():
                responses = self.schema(many=False)
                return {
                           'data': responses.dump(record)
                       }, 200
            return {
                       'message': 'data Documents not Found '
                   }, 404
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500
    
    def get_by_series_numbers(self, type, series, numbers):
        try:
            if record := self.model.where(id=id).first():
                responses = self.schema(many=False)
                return {
                           'data': responses.dump(record)
                       }, 200
            return {
                       'message': 'data Documents not Found '
                   }, 404
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def create(self, data):
        try:
            new_record = self.model.create(**data)
            new_record.where()
            db2.session.add(new_record)
            db2.session.commit()

            response = self.schema(many=False)

            return {
               'message': 'Successfully created',
               'data': response.dump(new_record)
                   }, 201
        except Exception as e:
            db2.session.rollback()
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                record.update(**data)
                db2.session.add(record)
                db2.session.commit()

                responses = self.schema(many=False)
                return {
                           'message': 'Document update successfully!',
                           'data': responses.dump(record)
                       }, 200
            return {
                       'message': 'data Document not Found '
                   }, 404
        except Exception as e:
            db2.session.rollback()
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():
                if record.status != "A":
                    record.update(status="A")
                    db2.session.add(record)
                    db2.session.commit()
                    return {
                               'message': 'disabled Document successfully'
                           }, 200
                return {
                    'message': 'Document is already deactivated'
                }, 200
            return {
                       'message': 'Document is not Found'
                   }, 404
        except Exception as e:
            db2.session.rollback()
            return {
                'message': 'An error occurred!',
                'error': str(e)
            }, 500
