from fastapi import APIRouter, HTTPException, Depends
from utils.auth import get_current_user
import cloudinary
import cloudinary.api
from dotenv import load_dotenv
import os

load_dotenv()

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

router = APIRouter()

@router.get("/view-uploads")
async def view_uploads(current_user: str = Depends(get_current_user)):
    try:
        # Fetch list of uploaded resources from Cloudinary
        response = cloudinary.api.resources(type="upload", resource_type="raw")
        
        # Extracting file URLs and other details
        uploaded_files = []
        for item in response.get("resources", []):
            file_info = {
                "public_id": item["public_id"],
                "url": item["secure_url"],
                "created_at": item["created_at"]
            }
            uploaded_files.append(file_info)
        
        # Return list of uploaded files
        return {"uploaded_files": uploaded_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
