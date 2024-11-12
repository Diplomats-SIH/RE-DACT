from fastapi import FastAPI, File, UploadFile
from typing import Dict

app = FastAPI()

# Supported content types
SUPPORTED_CONTENT_TYPES = [
    "image/jpeg", "image/png",  "image/jpg",       # Image formats
    "video/x-matroska", "video/mp4", # Video formats
    "application/pdf",               # PDF format
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"  # DOCX format
]

# Root endpoint to confirm server is running
@app.get("/")
async def root():
    return {"message": "FastAPI server is running!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> Dict[str, str]:
    if file.content_type not in SUPPORTED_CONTENT_TYPES:
        return {"status": "failed", "message": "Unsupported file type."}
    
    file_id = "12345"
    return {"file_id": file_id, "status": "uploaded"}
