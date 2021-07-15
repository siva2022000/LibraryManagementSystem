from typing import Optional
from fastapi import APIRouter,Depends
import schemas
from sqlalchemy.orm import Session
from repository import inventory
import database

#reference to current session
get_db = database.get_db

#reference to router related to inventory
router = APIRouter(
    prefix = "/inventory",
    tags = ["Inventory"]
)


#route to add books to the inventory database
@router.post("/",response_model=schemas.ShowInventory)
def add_book_to_inventory(request: schemas.Inventory,db: Session = Depends(get_db)):
    return inventory.add_book_to_inventory(request,db)


#route to display details of books in Inventory
@router.get("/")
def get_books_details(db:Session(get_db)= Depends(get_db)):
    return inventory.get_books_details(db)

#route to get details about specific book in inventory based on name
@router.get("/{title}")
def show_book_in_inventory(title:str,db:Session(get_db)= Depends(get_db)):
    return inventory.show_in_inventory(title,db)

#route to update row and total_copies column related to book with given title in inventory 
@router.put("/{title}")
def change_book_details(title:str,row:Optional[str]=None,total_copies:Optional[int] = None,db:Session(get_db)= Depends(get_db)):
    return inventory.change_details(title,db,row,total_copies)