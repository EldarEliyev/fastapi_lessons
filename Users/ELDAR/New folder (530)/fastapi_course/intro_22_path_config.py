from fastapi import FastAPI, status 
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()

class Phone(BaseModel):
    brand: str 
    model : str 
    price: float 
    description: Optional[str] = None


@app.post("/phones/",  response_model=Phone, status_code=status.HTTP_201_CREATED,  tags=["Phones"],  summary="Create a new phone",  description="This endpoint allows you to create a new phone with the specified details.",  response_description="The created phone details")
async def create_phone(phone: Phone):
    return phone 


@app.get("/users/",  tags=["Users"],  deprecated=True)
async def read_user():
    return [{"username":  "eldar_aliyev"}]