from fastapi import FastAPI
import models
from database import engine
from routers import book,inventory,student

#refernce to start the server 
app = FastAPI()

#creates tables using in the libray_db database using models defined in models class
models.Base.metadata.create_all(engine)

#adds routes to the server
app.include_router(book.router)
app.include_router(inventory.router)

app.include_router(student.router)