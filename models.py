from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func



#sqlalchemy model for book
class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating = Column(Integer)
    author = Column(String)
    category = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    inventory = relationship('Inventory', back_populates='item')

#sqlalchemy model for inventory
class Inventory(Base):
    __tablename__ =  "inventory"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer,ForeignKey("book.id"))
    total_copies = Column(Integer)
    shelf = Column(String)
    cover_type = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    issues = Column(String)
    
    item = relationship('Book', back_populates='inventory')



    
    
    