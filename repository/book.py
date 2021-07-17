import models
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status


#adds book to the database
def add_book(request: schemas.Book,db: Session):

    #adds book to books table
    new_book = models.Book(title=request.title, rating=request.rating, author=request.author,category = request.category)
    db.add(new_book)
    db.commit()
    
    #creates a row related to  that book in inventory table
    new_book_in_inventory = models.Inventory(book_id = new_book.id)
    db.add(new_book_in_inventory)
    db.commit()
    db.refresh(new_book)
    return new_book

#returns details of all the books in books table
def get_all_books(db:Session):    
    return db.query(models.Book).all()

#returns details related to the book
def show(title:str,db:Session):
    book = db.query(models.Book).filter(models.Book.title == title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not available')
    return book

