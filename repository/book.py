from models import Book as ModelBook
from schema import Book as SchemaBook
from sqlalchemy.orm import Session
from fastapi import Depends



def add_book(request: SchemaBook,db: Session):
    db_book = ModelBook(title=request.title, rating=request.rating, author=request.author,category = request.category)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book