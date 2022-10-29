from app import app, db2
from app import routers
from app.models.base import BaseModel
BaseModel.set_session(db2.session)