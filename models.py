from sqlalchemy import Column, Integer, String
from database import Base

#model/table
class Item(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
    status = Column(String(20))