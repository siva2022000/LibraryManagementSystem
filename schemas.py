from pydantic import BaseModel

#pydantic schema for book
class Book(BaseModel):
    title: str
    rating: int
    author:str
    category:str

    class Config:
        orm_mode = True

#pydantic schema for inventory
class Inventory(BaseModel):
    book_title:str
    total_copies: int
    shelf:str
    cover_type:str

    class Config:
        orm_mode = True

#pydantic schema for student
class Student(BaseModel):
    name:str
    age:int
    gender:str

    class Config:
        orm_mode = True        

class ShowInventory(BaseModel):
    total_copies: int
    shelf:str
    cover_type:str
    
    class Config:
        orm_mode = True
