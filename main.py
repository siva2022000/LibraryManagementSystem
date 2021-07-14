from fastapi import FastAPI
import models
from database import engine
from routers import book

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(book.router)

