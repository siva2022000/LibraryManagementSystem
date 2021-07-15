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