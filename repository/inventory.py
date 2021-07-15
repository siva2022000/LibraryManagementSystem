from repository import book
import models
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends


#adds book to the inventory
def add_book_to_inventory(request: schemas.Inventory,db: Session):
    book_title = request.book_title
    book_item = db.query(models.Book).filter(models.Book.title == book_title).first()

    new_item = models.Inventory(book_id = book_item.id,
     total_copies=request.total_copies, shelf=request.shelf,cover_type = request.cover_type)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item