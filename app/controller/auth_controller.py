from app import db2
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from secrets import token_hex
from app.utils.mailing import Mailing

class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schema = ''
        self.mailing = Mailing()

    def sign_in(self, data):
        try:
            if record := self.model.where(
                    user_name=data.get('user_name'),
                    status=True
                    ).first():
                if record.check_password(data.get('password')):
                    access_token = create_access_token(identity=record.id),
                    access_refresh_token = create_refresh_token(identity=record.id)
                    return{
                        'access token': access_token,
                        'refresh token': access_refresh_token
                    }
                else:
                    raise Exception('password incorrect')
            raise Exception('The user was not found')
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def reset_password(self, data):
        try:
            if record := self.model.where(
                    email=data.get('email'),
                    status=True
            ).first():
                new_password = token_hex(5)
                record.password = new_password
                record.hash_password()
                self.mailing.email_reset_password(record.email, new_password)

                db2.session.add(record)
                db2.session.commit()

                return {
                    'message': 'an email was sent with the new password'
                }, 200
            raise Exception('User not found')
        except Exception as e:
            db2.session.rollback()
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500

    def refresh_token(self, identity):
        try:
            access_token = create_access_token(
                identity=identity
                )
            return {
                        'access token': access_token
                    }, 200
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500


