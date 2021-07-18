
import models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import Optional





#returns the details of all books in inventory table
def get_books_details(db:Session):    
    return db.query(models.Inventory,models.Book.title).\
        filter(models.Inventory.book_id == models.Book.id).all()

#returns details related to the book with given name in inventory
def show_in_inventory(title:str,db:Session):
    book = db.query(models.Book).filter(models.Book.title == title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not present')
    in_book = db.query(models.Inventory).filter(models.Inventory.book_id == book.id).first()
    
    return in_book

#code to update number of copies in inventory
def update_details(title:str,db:Session,copies:int):

    #the book with given title is found in books table
    book = db.query(models.Book).filter(models.Book.title == title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with title {title} is not found. First add the book')

    #search for the book in inventory table using its id                         
    new_book = db.query(models.Inventory).filter(models.Inventory.book_id == book.id).first()
    
    #adds the copies count to total_copies
    new_book.total_copies+=copies
    new_book.available_copies+=copies
    db.commit()
    return 'updated'

#code that returns the list of books with most number of issues
def get_popular_books(db:Session):
    #inner join Book and Inventory tables and display titles and total_issues columns
    return db.query(models.Book.title,models.Inventory.total_issues).filter(models.Inventory.book_id == models.Book.id).\
        order_by(models.Inventory.total_issues.desc()).limit(5).all()
