from os import getenv
from flask import Flask
from flask_restx import Api
from config import config_env
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder='templates')
app.config.from_object(config_env[getenv('FLASK_ENV')])
api2 = Api(
  app,
  title='Collect SGI',
  version='1.0.0',
  description='Endpoints SGI',
  doc='/swagger-ui-sgi'
)
db2 = SQLAlchemy(app)
migrate = Migrate(app, db2)
