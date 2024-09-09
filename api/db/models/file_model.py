from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    original_filename = Column(String)
    file_path = Column(String)
    file_type = Column(String)
    upload_time = Column(DateTime(timezone=True), server_default=func.now())
    transcription = Column(String, nullable=True)
    generated_text = Column(String, nullable=True)