from fastapi import APIRouter,Depends
from schema import Book as SchemaBook
from sqlalchemy.orm import Session
from repository import book
import database

get_db = database.get_db
router = APIRouter(
    prefix = "/book",
    tags = ["Book"]
)



@router.post("/", response_model=SchemaBook)
def add_book(request: SchemaBook,db: Session = Depends(get_db)):
    return book.add_book(request,db)