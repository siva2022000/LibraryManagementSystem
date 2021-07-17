from sqlalchemy.sql.functions import func
from starlette.status import HTTP_400_BAD_REQUEST
import models
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status


#registers student
def register_student(request: schemas.Student,db: Session):
    new_student = models.Student(name = request.name,age = request.age,gender = request.gender)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

#returns the details of all the students registered
def get_list(db:Session):    
    return db.query(models.Student).all()

#returns details related to the student with given name
def get_details(name:str,db:Session):
    student = db.query(models.Student).filter(models.Student.name == name).first()

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Student with given name {name} does not exist')                        
    return student

#issues book to the student
def issue_book(student_name:str,book_title:str,db:Session):
    student = db.query(models.Student).filter(models.Student.name == student_name).first()
    book = db.query(models.Inventory).filter(models.Inventory.book_title == book_title).first()
    item = db.query(models.Inventory).filter(models.Inventory.book_title == book_title).first()
    issue_item = models.Issue_log(book_id = book.id,student_id=student.id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Student with given name {student_name} does not exist')
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Book with given title {book_title} does not exist')

    if book.available_copies == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail = f'This book is not available currrently')                                            
    if student.books_count == 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail = f'Books issued by this student has reached maximum limit')
    
    student.books_count = student.books_count + 1
    book.available_copies = book.available_copies - 1
    item.total_issues+=1
    db.add(issue_item)
    
    db.commit()
    return f'{book_title} is issued to {student_name}' 

def return_book(student_name:str,book_title:str,db:Session):
    student = db.query(models.Student).filter(models.Student.name == student_name).first()
    book = db.query(models.Inventory).filter(models.Inventory.book_title == book_title).first()
    issue_item = db.query(models.Issue_log).filter(models.Issue_log.book_id == book.id and models.Issue_log.student_id == student.id).first()
    if not issue_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail = f'Book {book_title} is not issued to student {student_name}')

    student.books_count = student.books_count - 1
    book.available_copies = book.available_copies + 1
    issue_item.return_time = func.now()
    db.commit()
    return f'{book_title} is returned to {student_name}'       
                            
