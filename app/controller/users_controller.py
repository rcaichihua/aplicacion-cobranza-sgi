from app import db2
from app.models.users_model import UserModel
from app.schemas.users_schema import UsersResponseSchema


class UsersController:
    def __init__(self):
        self.model = UserModel
        self.schema = UsersResponseSchema

    def all(self):
        try:
            records = self.model.where(status=True).order_by('id').all()
            response = self.schema(many=True)
            return {
                'data': response.dump(records)
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
                       'message': 'data Role not Found '
                   }, 404
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def create(self, data):
        try:
            new_record = self.model.create(**data)
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
                           'message': 'data Role update successfully!',
                           'data': responses.dump(record)
                       }, 200
            return {
                       'message': 'data Role not Found '
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
                               'message': 'disabled rol successfully'
                           }, 200
                return {
                    'message': 'role is already deactivated'
                }, 200
            return {
                       'message': 'Role Id not Found '
                   }, 404
        except Exception as e:
            db2.session.rollback()
            return {
                'message': 'An error occurred!',
                'error': str(e)
            }, 500
