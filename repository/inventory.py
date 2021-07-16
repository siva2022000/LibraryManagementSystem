from sqlalchemy.sql.functions import mode
import models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import Optional





#returns the details of books in inventory table
def get_books_details(db:Session):    
    return db.query(models.Inventory).all()

#returns details related to the book in inventory
def show_in_inventory(title:str,db:Session):
    book = db.query(models.Inventory).filter(models.Inventory.book_title == title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not present in Inventory')
    return book

def update_details(title:str,db:Session,row:Optional[str]=None,copies:Optional[int] = None):
    new_book = db.query(models.Inventory).filter(models.Inventory.book_title == title)
    if not new_book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not found in inventory')
    if row:                        
        new_book.update({"shelf" : row})
          
    if copies:                        
        new_book.update({"total_copies" : copies,"available_copies": copies})  
    db.commit()
    return 'updated'

def get_popular_books(db:Session):
    return db.query(models.Inventory.book_title,models.Inventory.total_issues).order_by(models.Inventory.total_issues.desc()).limit(5).all()   