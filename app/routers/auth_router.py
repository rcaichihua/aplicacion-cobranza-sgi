from app import api2


auth_ns = api2.namespace(
    name='authentication',
    description='Authentication module path',
    path='/auth'
)