from app import db2
from sqlalchemy import Column, Integer, String

class Area(db2.Model):
    __tablename__ = "area"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))