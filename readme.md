# Library Management System

##### Abstract

This application provides apis for adding books into the database, updating inventory, registering students, issue books present in inventory to students and getting details about top five popular books

---

##### Folder Structure

LIBRARYMANAGEMENTSYSTEM

|   __init__.py
|   .gitignore
|   database.py
|   library_db.db
|   main.py
|   models.py
|   pyproject.toml
|   readme.md
|   schemas.py
|
+---repository
|       book.py
|       inventory.py
|       student.py
|       __init__.py
|
\\---routers
      book.py
      inventory.py
      student.py
      __init__.py

---

##### Requirements

* python
* poetry

---

##### Installation and Running Server in ubuntu
1. create a python environment

   > -$ python3 -m venv .venv
   >
2. Activate the python environment using following command

   > -$ source .venv/bin/activate
   >
3. Run the following command to install all the packages and dependencies

   > -$ poetry install
   >

4. Code to run the server

   > -$ uvicorn main:app --reload
   >

---

##### Database Tables structure

* ###### books

  | column_name     | data_type | is_nullable | column_default    | foreign_key |
  | --------------- | --------- | ----------- | ----------------- | ----------- |
  | id(primary_key) | INTEGER   | NO          | NULL              |             |
  | title           | VARCHAR   | YES         | NULL              |             |
  | time_created    | DATETIME  | YES         | CURRENT_TIMESTAMP |             |
  | rating          | INTEGER   | YES         | NULL              |             |
  | author          | VARCHAR   | YES         | NULL              |             |
  | category        | VARCHAR   | YES         | NULL              |             |
* ###### inventory

  | column_name      | data_type | is_nullable | column_default    | foreign_key |
  | ---------------- | --------- | ----------- | ----------------- | ----------- |
  | id(primary_key)  | INTEGER   | NO          | NULL              |             |
  | book_id          | INTEGER   | YES         | NULL              | books(id)   |
  | total_copies     | INTEGER   | YES         | NULL              |             |
  | available_copies | INTEGER   | YES         | NULL              |             |
  | time_created     | DATETIME  | YES         | CURRENT_TIMESTAMP |             |
  | time_updated     | DATETIME  | YES         | NULL              |             |
  | total_issues     | INTEGER   | YES         | NULL              |             |
* ###### students

  | column_name     | data_type | is_nullable |
  | --------------- | --------- | ----------- |
  | age             | INTEGER   | YES         |
  | gender          | VARCHAR   | YES         |
  | name            | VARCHAR   | YES         |
  | books_count     | INTEGER   | YES         |
  | id(primary_key) | INTEGER   | NO          |
* ###### issue_log

  | column_name | data_type | is_nullable | column_default    | foreign_key  |
  | ----------- | --------- | ----------- | ----------------- | ------------ |
  | student_id  | INTEGER   | YES         | NULL              | students(id) |
  | id          | INTEGER   | NO          | NULL              |              |
  | book_id     | INTEGER   | YES         | NULL              | books(id)    |
  | return_time | DATETIME  | YES         | NULL              |              |
  | issued_time | DATETIME  | YES         | CURRENT_TIMESTAMP |              |

---

##### Additional Details

* "main.py" file - contains contains app variable which is a reference to the instance of FastAPI class. It is the main point of interaction for creating APIs
* "database.py" file- contains code which creates a database session
* "library_db.db" - database
* "models.py" file - contains models for database tables
* "schemas.py" file - contains pydantic schemas
* "pyproject.toml" file - used to install packages and dependencies
* "routes" folder - contains files which contain code related to different api endpoints
* "repository" folder - contains files which provide functionalities to the different api endpoints in router folder
* connect to fastapi swagger ui using http://localhost:8000/docs

---
