from pydantic import BaseModel, ConfigDict
from datetime import datetime

class FileBase(BaseModel):
    filename: str
    original_filename: str
    file_path: str
    file_type: str

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    upload_time: datetime
    transcription: str | None = None
    generated_text: str | None = None

    model_config = ConfigDict(from_attributes=True)
