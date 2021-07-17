from re import I
from repository import book
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func



#sqlalchemy model for book
class Book(Base):
    __tablename__ = "books"
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
    book_id = Column(Integer,ForeignKey("books.id"))
    book_title = Column(String)
    total_copies = Column(Integer,default=0)
    available_copies = Column(Integer,default=0)
    shelf = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    total_issues = Column(Integer,default=0)
    
    item = relationship('Book', back_populates='inventory')


#sqlalchemy model for students table
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    books_count = Column(Integer,default=0)

#sqlalchemy model for table which store date about books issue    
class Issue_log(Base):
    __tablename__ = "issue_log"
    id = id = Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("books.id"))
    student_id = Column(Integer,ForeignKey("students.id"))
    issued_time = Column(DateTime(timezone=True), server_default=func.now())
    return_time = Column(DateTime(timezone=True), onupdate=func.now())


    
    
    