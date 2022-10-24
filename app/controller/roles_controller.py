from app import db2
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RolesResponseSchema


class RolesController:
    def __init__(self):
        self.model = RoleModel
        self.schema = RolesResponseSchema

    def all(self):
        try:
            records = self.model.all()
            response = self.schema(many=True)
            return{
                'data': response.dump(records)
            }
        except Exception as e:
            return{
                'message': 'An error occurred!',
                'error': str(e)
            }, 500



    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db2.session.add(new_record)
            db2.session.commit()

            response = self.schema(many=False)

            return{
                'message': 'Successfully created',
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            db2.session.rollback()
            return{
                'message': 'An error occurred!',
                'error': str(e)
            }, 500
