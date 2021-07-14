from pydantic import BaseModel


class Book(BaseModel):
    title: str
    rating: int
    author:str
    category:str

    class Config:
        orm_mode = True