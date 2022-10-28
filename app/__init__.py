from os import getenv
from flask import Flask
from flask_restx import Api
from config import config_env
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates')
app.config.from_object(config_env[getenv('FLASK_ENV')])
#Se cambia a apikey por Bearer
authorization = {
  'Bearer' : {
      'type': 'apiKey',
      'in': 'header',
      'name': 'Authorization'
  }
}

api2 = Api(
  app,
  title='Collect SGI',
  version='1.0.0',
  description='Endpoints SGI',
  #security='apikey',
  authorizations=authorization,
  doc='/swagger-ui-sgi'
)
db2 = SQLAlchemy(app)
migrate = Migrate(app, db2)

jwt = JWTManager(app)