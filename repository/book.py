import models
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends


#adds book to the database
def add_book(request: schemas.Book,db: Session):
    new_book = models.Book(title=request.title, rating=request.rating, author=request.author,category = request.category)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

