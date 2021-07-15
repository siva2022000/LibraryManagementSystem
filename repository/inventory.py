import models
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import Optional


#adds book to the inventory
def add_book_to_inventory(request: schemas.Inventory,db: Session):
    book_title = request.book_title
    book_item = db.query(models.Book).filter(models.Book.title == book_title).first()
    if not book_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {request.book_title} is not present in book table. First add this book to the list of books')
    new_item = models.Inventory(book_id = book_item.id,
     total_copies=request.total_copies, shelf=request.shelf,cover_type = request.cover_type)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


#returns the details of books in inventory table
def get_books_details(db:Session):    
    return db.query(models.Inventory).all()

#returns details related to the book in inventory
def show_in_inventory(title:str,db:Session):
    book_item = db.query(models.Book).filter(models.Book.title == title).first()
    book = db.query(models.Inventory).filter(models.Inventory.book_id == book_item.id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not present in Inventory')
    return book

def change_details(title:str,db:Session,row:Optional[str]=None,copies:Optional[int] = None):
    book_item = db.query(models.Book).filter(models.Book.title == title).first()
    if not book_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not found in Books list')
    new_book = db.query(models.Inventory).filter(models.Inventory.book_id == book_item.id)
    if not new_book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not found in inventory')
    if row:                        
        new_book.update({"shelf" : row})
          
    if copies:                        
        new_book.update({"total_copies" : copies})  
    db.commit()
    return 'updated'   