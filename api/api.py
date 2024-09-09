from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import shutil
import os
import hashlib
from uuid import uuid4
from .db.crud import create_file, get_file, get_files, update_file_original_filename, get_file_by_hash
from .db.database import SessionLocal, engine, get_db
from .db.models.file_model import File as FileModel
from .db.schemas import FileCreate, File as FileSchema
from .routers import payments, ai_processing
# Create tables
FileModel.__table__.create(bind=engine, checkfirst=True)


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(payments.router, prefix="/api/payments", tags=["Payments"])
app.include_router(ai_processing.router, prefix="/api/ai", tags=["AI Processing"])

# Create a directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)



        
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.post("/upload", response_model=FileSchema, tags=["Files"])
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Generate file hash
        file_content = await file.read()
        file_hash = hashlib.md5(file_content).hexdigest()
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"{file_hash}{file_extension}"

        # Check if file with the same hash already exists
        existing_file = get_file_by_hash(db, file_hash)
        
        if existing_file:
            # Update original_filename if it's different
            updated_file = update_file_original_filename(db, existing_file.id, file.filename)
            return updated_file

        file_location = os.path.join(UPLOAD_DIR, unique_filename)
        
        # Save the file
        with open(file_location, "wb") as file_object:
            file_object.write(file_content)
        
        # Create file record in database
        file_data = FileCreate(
            filename=unique_filename,
            original_filename=file.filename,
            file_path=file_location,
            file_type=file.content_type
        )
        db_file = create_file(db, file_data)
        
        return db_file
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/files", response_model=list[FileSchema], tags=["Files"])
def get_all_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    files = get_files(db, skip=skip, limit=limit)
    return files

@app.get("/files/{file_id}", response_model=FileSchema, tags=["Files"])
def get_single_file(file_id: int, db: Session = Depends(get_db)):
    db_file = get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file