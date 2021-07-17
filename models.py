from sqlalchemy.sql.expression import column
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

    inventory = relationship('Inventory', back_populates='books')

#sqlalchemy model for inventory
class Inventory(Base):
    __tablename__ =  "inventory"
    id = Column(Integer, primary_key=True, index=True)

    #stores primary key of books table as foreign key
    book_id = Column(Integer,ForeignKey("books.id"))

    # total number of copies that should be present in the library 
    total_copies = Column(Integer,default=0)

    #number of copies currently available in inventory after issuing some copies 
    available_copies = Column(Integer,default=0)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    #no of times students have issued the book 
    total_issues = Column(Integer,default=0)
    
    books = relationship('Book', back_populates='inventory')


#sqlalchemy model for students table
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    #no of books present with the student
    books_count = Column(Integer,default=0)

#sqlalchemy model for table which store date about books issues    
class Issue_log(Base):
    __tablename__ = "issue_log"
    id = id = Column(Integer,primary_key=True,index=True)
    book_id = Column(Integer,ForeignKey("books.id"))
    student_id = Column(Integer,ForeignKey("students.id"))
    issued_time = Column(DateTime(timezone=True), server_default=func.now())
    return_time = Column(DateTime(timezone=True), onupdate=func.now())


    
    
    