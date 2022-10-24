from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    last_name = Column(String(160))
    user_name = Column(String(80), unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(50), unique=True)
    status = Column(Boolean)
    rol_id = Column(Integer, ForeignKey('roles.id'), default=1)

