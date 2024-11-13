from fastapi import APIRouter, HTTPException, Form
from datetime import timedelta
from utils.auth import create_access_token

router = APIRouter()

@router.post("/token")
async def login(username: str = Form(...), password: str = Form(...)):
    # This is a simple validation, replace it with real authentication logic
    if username == "admin" and password == "password":  # Example credentials
        access_token_expires = timedelta(minutes=15)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
