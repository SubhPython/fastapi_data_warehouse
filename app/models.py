from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    data = Column(JSON)

class Campaign(Base):
    __tablename__ = 'campaigns'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    data = Column(JSON)
