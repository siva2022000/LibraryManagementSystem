from fastapi import APIRouter,Depends
import schemas
from sqlalchemy.orm import Session
from repository import student
import database

#reference to current session
get_db = database.get_db

#reference to router related to student
router = APIRouter(
    prefix = "/student",
    tags = ["Student"]
)


#route to register student in the database
@router.post("/")
def register_student(request: schemas.Student,db: Session = Depends(get_db)):
    return student.register_student(request,db)

#route to display details of all students registered
@router.get("/")
def get_all_students_list(db:Session(get_db)= Depends(get_db)):
    return student.get_list(db)

#route to get details about specific student based on name
@router.get("/{name}")
def get_student_details(name:str,db:Session(get_db)= Depends(get_db)):
    return student.get_details(name,db) 

@router.put("/{student_name}/issue_book")
def issue_book(student_name:str,book_title:str,db:Session(get_db) = Depends(get_db)):
    return student.issue_book(student_name,book_title,db)

