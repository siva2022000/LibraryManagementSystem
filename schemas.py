from pydantic import BaseModel

#pydantic schema for book
class Book(BaseModel):
    title: str
    rating: int
    author:str
    category:str

    class Config:
        orm_mode = True


#pydantic schema for student
class Student(BaseModel):
    name:str
    age:int
    gender:str

    class Config:
        orm_mode = True        
