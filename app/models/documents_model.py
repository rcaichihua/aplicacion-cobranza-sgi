from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class DocumentModel(BaseModel):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_doc = Column(String(2))
    series = Column(String(4), nullable=False)
    number = Column(String(8), nullable=False)
    issue_date = Column(String(10), nullable=False)
    collect_date = Column(String(10), nullable=True)
    process_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now)
    amount = Column(String, nullable=False, default="0.00")
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String, default='P') #P pendiente A anulado C cancelado

    user = relationship('UserModel', uselist=False, back_populates='documents')
