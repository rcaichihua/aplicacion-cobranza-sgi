from app.models.users_model import UserModel


class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schema = ''

    def sign_in(self, data):
        try:
            if record := self.model.where(
                    user_name=data.get('user_name'),
                    status=True
                    ).first():
                if record.check_password(data.get('password')):
                    return {
                        'message': 'Yes user exist'
                    }
                else:
                    raise Exception('password incorrect')
            raise Exception('The user was not found')
        except Exception as e:
            return {
                       'message': 'An error occurred!',
                       'error': str(e)
                   }, 500


