from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class RoleModel(BaseModel):
    __tablename__='roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    status = Column(Boolean, default=True)

    users = relationship('UserModel', uselist=True, back_populates='role')
