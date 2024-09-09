# Backend Setup Instructions

Use this guide to setup the backend for this project.

It uses FastAPI, SQLAlchemy, Pydantic, and RESTful API design principles.

Write the complete code for every step. Do not get lazy. Write everything that is needed.

Your goal is to completely finish the backend setup.

## Helpful Links

If the user gets stuck, refer them to the following links:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [RESTful API Design Principles](https://restfulapi.net/rest-architectural-constraints/)


## Install Libraries

Make sure the user knows to install the python packages:

```bash
pip install fastapi sqlalchemy pydantic
```

## Setup Steps

- Create a `/api` folder in the root of the project

- Create a `/api/db` folder in the root of the project

- Add a `api.py` file to the `/api` folder with the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

- Add a file called `database.py` to the `/api/db` folder with the following code:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

- Create a new folder called `/models` in the `/api/db` folder

- Create an example model in the `/models` folder called `example-model.py` with the following code:

```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Example(Base):
    __tablename__ = "example"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False) 

    def __repr__(self):
        return f"<Example(name='{self.name}', age='{self.age}', email='{self.email}')>"
```

- Create a new folder called `/schemas` in the `/api/db` folder

- Create an example schema in the `/schemas` folder called `example-schema.py` with the following code: 

```python
from pydantic import BaseModel

class ExampleSchema(BaseModel):
    name: str
    age: int
    email: str

```

- Create a new folder called `/crud` in the `/api/db` folder

- Create an example crud in the `/crud` folder called `example-crud.py` with the following code:

```python
from sqlalchemy.orm import Session
from . import models, schemas

def get_all_examples(db: Session):
    return db.query(models.Example).all()

def get_example_by_id(db: Session, example_id: int):
    return db.query(models.Example).filter(models.Example.id == example_id).first()

def create_example(db: Session, example: schemas.ExampleSchema):
    db_example = models.Example(name=example.name, age=example.age, email=example.email)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

def update_example(db: Session, example_id: int, example: schemas.ExampleSchema):
    db_example = db.query(models.Example).filter(models.Example.id == example_id).first()
    if db_example:
        db_example.name = example.name
        db_example.age = example.age
        db_example.email = example.email
        db.commit() 
        db.refresh(db_example)
    return db_example

def delete_example(db: Session, example_id: int):
    db_example = db.query(models.Example).filter(models.Example.id == example_id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
    return db_example
```

- Create a `requirements.txt` file in the `/api` folder
- In `api/requirements.txt`, add the following packages:

```txt
fastapi
sqlalchemy
pydantic
uvicorn
```

- The backend is now setup.
