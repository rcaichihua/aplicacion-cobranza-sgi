from app import db2
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class AreaModel(db2.Model):
    id: int
    name: str

    __tablename__ = "area"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
