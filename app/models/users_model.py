from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from bcrypt import hashpw, gensalt, checkpw


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code_debd_collector = Column(String(20))
    name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50), unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(50), unique=True)
    status = Column(Boolean, default=True)
    rol_id = Column(Integer, ForeignKey('roles.id'), default=2)

    role = relationship('RoleModel', uselist=False, back_populates='users')

    def hash_password(self):
        password_encode = self.password.encode('utf-8')
        password_hash = hashpw(password_encode, gensalt(rounds=10))
        self.password = password_hash.decode('utf8')

    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
