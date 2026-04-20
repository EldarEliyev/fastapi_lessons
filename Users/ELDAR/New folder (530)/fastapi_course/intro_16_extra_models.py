from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None 


class UserCreate(UserBase):
    password: str 


class UserRead(UserBase):
    id: int 


fake_db = []

@app.post("/users/",  response_model=UserRead)
async def create_user(user: UserCreate):
    new_user_id = len(fake_db) + 1 
    user_data = user.dict()
    user_data.update({"id": new_user_id})

    fake_db.append(user_data)

    return user_data