from app import db2
from app.models.users_model import UserModel
from app.schemas.users_schema import UsersResponseSchema


class UsersController:
    def __init__(self):
        self.model = UserModel
        self.schema = UsersResponseSchema

    def all(self, page, per_page):
        try:
            records = self.model.where(status=True).order_by('id').paginate(
                per_page=per_page, page=page
            )
            response = self.schema(many=True)
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
                       'message': 'data User not Found '
                   }, 404
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def create(self, data):
        try:
            new_record = self.model.create(**data)
            new_record.hash_password()
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
                record.hash_password()
                db2.session.add(record)
                db2.session.commit()

                responses = self.schema(many=False)
                return {
                           'message': 'data User update successfully!',
                           'data': responses.dump(record)
                       }, 200
            return {
                       'message': 'data User not Found '
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
                if record.status:
                    record.update(status=False)
                    db2.session.add(record)
                    db2.session.commit()
                    return {
                               'message': 'disabled user successfully'
                           }, 200
                return {
                    'message': 'User is already deactivated'
                }, 200
            return {
                       'message': 'User Id not Found '
                   }, 404
        except Exception as e:
            db2.session.rollback()
            return {
                'message': 'An error occurred!',
                'error': str(e)
            }, 500
