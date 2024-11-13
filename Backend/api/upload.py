from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from cloudinary.uploader import upload
import cloudinary
from utils.auth import get_current_user
from utils.encryption import encrypt_file_content
import os
from dotenv import load_dotenv

load_dotenv()

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

router = APIRouter()

# Supported file types
ALLOWED_FILE_TYPES = {
    "image/jpeg",   # .jpeg 
    "image/jpg",    # .jpg
    "image/png",    # .png
    "application/pdf",  # .pdf
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # .docx
    "video/mp4",    # .mp4
    "video/x-matroska"  # .mkv
}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), current_user: str = Depends(get_current_user)):
    # Validate file type
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    try:
        # Read and encrypt file content
        file_content = await file.read()
        encrypted_content = encrypt_file_content(file_content)

        # Upload encrypted content to Cloudinary
        result = upload(encrypted_content, resource_type="raw")
        
        # Return Cloudinary secure URL
        return {"url": result["secure_url"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
