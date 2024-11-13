from fastapi import FastAPI
from api.upload import router as upload_router
from api.login import router as login_router
from api.view import router as view_router

app = FastAPI()

# Include the routers
app.include_router(upload_router, prefix="/api", tags=["Uploads"])
app.include_router(login_router, prefix="/api", tags=["Authentication"])
app.include_router(view_router, prefix="/api", tags=["ViewUploads"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with Cloudinary!"}
