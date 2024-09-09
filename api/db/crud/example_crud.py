from sqlalchemy.orm import Session
from ..models import example_model
from ..schemas import example_schema

def get_all_examples(db: Session):
    return db.query(example_model.Example).all()

def get_example_by_id(db: Session, example_id: int):
    return db.query(example_model.Example).filter(example_model.Example.id == example_id).first()

def create_example(db: Session, example: example_schema.ExampleSchema):
    db_example = example_model.Example(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

def update_example(db: Session, example_id: int, example: example_schema.ExampleSchema):
    db_example = db.query(example_model.Example).filter(example_model.Example.id == example_id).first()
    if db_example:
        for key, value in example.dict().items():
            setattr(db_example, key, value)
        db.commit()
        db.refresh(db_example)
    return db_example

def delete_example(db: Session, example_id: int):
    db_example = db.query(example_model.Example).filter(example_model.Example.id == example_id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
    return db_example