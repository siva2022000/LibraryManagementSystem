from fastapi import APIRouter,Depends
import schemas
from sqlalchemy.orm import Session
from repository import book
import database

#reference to current session
get_db = database.get_db

#reference to router related to books
router = APIRouter(
    prefix = "/book",
    tags = ["Book"]
)


#route to add books to the database
@router.post("/")
def add_book(request: schemas.Book,db: Session = Depends(get_db)):
    return book.add_book(request,db)

#route to display all the books in Book table
@router.get("/")
def get_all_books(db:Session(get_db)= Depends(get_db)):
    return book.get_all_books(db)

#route to get details about specific book based on name
@router.get("/{title}")
def show_book(title:str,db:Session(get_db)= Depends(get_db)):
    return book.show(title,db)

@router.delete("/{title}")
def remove_book(title:str,db:Session(get_db)= Depends(get_db)):
    return book.remove_book(title,db)     


