from fastapi import FastAPI, File, Form, UploadFile
from typing import Optional


app = FastAPI()


@app.post("/profile/")
async def create_profile(username: str = Form(...),  email: str = Form(...),  age: Optional[int] = Form(None),  profile_picture: UploadFile = File(...)):
    return {
        "username": username,
        "email": email,
        "age": age,
        "file_name": profile_picture.filename,
        "content_type": profile_picture.content_type
    }