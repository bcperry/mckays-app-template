from sqlalchemy.orm import Session
from ..models.file_model import File
from ..schemas import FileCreate

def create_file(db: Session, file: FileCreate):
    db_file = File(**file.dict())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_file(db: Session, file_id: int):
    return db.query(File).filter(File.id == file_id).first()

def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(File).offset(skip).limit(limit).all()

def update_file(db: Session, file_id: int, file: FileCreate):
    db_file = db.query(File).filter(File.id == file_id).first()
    if db_file:
        for key, value in file.dict().items():
            setattr(db_file, key, value)
        db.commit()
        db.refresh(db_file)
    return db_file

def update_file_original_filename(db: Session, file_id: int, new_filename: str):
    db_file = db.query(File).filter(File.id == file_id).first()
    if db_file:
        if new_filename not in db_file.original_filename:
            db_file.original_filename = f"{db_file.original_filename}, {new_filename}"
            db.commit()
            db.refresh(db_file)
    return db_file

def get_file_by_hash(db: Session, file_hash: str):
    return db.query(File).filter(File.filename.startswith(file_hash)).first()