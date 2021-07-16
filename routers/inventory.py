from typing import Optional
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from repository import inventory
import database
import schemas
#reference to current session
get_db = database.get_db

#reference to router related to inventory
router = APIRouter(
    prefix = "/inventory",
    tags = ["Inventory"]
)

#route to update row and total_copies column related to book with given title in inventory 
@router.put("/{title}")
def update_book_details(title:str,row:Optional[str]=None,total_copies:Optional[int] = None,db:Session(get_db)= Depends(get_db)):
    return inventory.update_details(title,db,row,total_copies)


#route to display details of books in Inventory
@router.get("/")
def get_all_books_details(db:Session(get_db)= Depends(get_db)):
    return inventory.get_books_details(db)


@router.get("/popular_books")
def get_popular_books(db:Session(get_db)= Depends(get_db)):
    return inventory.get_popular_books(db)

#route to get details about specific book in inventory based on name
@router.get("/{title}")
def show_book_in_inventory(title:str,db:Session(get_db)= Depends(get_db)):
    return inventory.show_in_inventory(title,db)



