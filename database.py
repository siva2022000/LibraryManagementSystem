from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

#defining database url 
SQLALCHAMY_DATABASE_URL = 'sqlite:///./library_db.db'


#creates SQLAlchemy engine
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

#Instance of database session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

#function that returns current session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
