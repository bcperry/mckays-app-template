from sqlalchemy import Column, Integer, String
from api.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)