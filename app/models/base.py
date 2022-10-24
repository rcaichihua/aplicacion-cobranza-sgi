from app import db2
from sqlalchemy_mixins import AllFeaturesMixin


class BaseModel(db2.Model, AllFeaturesMixin):
    __abstract__ = True

