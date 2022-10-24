from app import app, db2, api2
from flask_restx import Resource

global_ns = api2.namespace(
    name='Global',
    description='Global routers',
    path='/globals'
)


@global_ns.route('/')
class Global(Resource):
    def get(self):
        return {
            'message': 'Hello world!'
        }

    @staticmethod
    def post():
        return {
            'message': 'Post'
        }


@global_ns.route('/<int:id>')
class GlobalGetById(Resource):
    def get(self, id):
        return {
            'message': f'ID: {id}'
        }

    def put(self, id):
        return {
            'message': f'ID update {id}'
        }

    def delete(self, id):
        return {
            'message': f'ID delete {id}'
        }


api2.add_namespace(global_ns)

# @app.route('/test', methods=['GET'])
# def index_2():
#    result = db2.engine.execute('select version();')
#    print(result.fetchone()[0])
#    return {
#        'Message': 'Prueba'
#    }
