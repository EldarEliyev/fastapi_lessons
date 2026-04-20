from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Computer(BaseModel):
    brand: str 
    model: str 
    description: Optional[str] = None 
    price: float
    tax: Optional[float] = None  

class User(BaseModel):
    username: str 
    full_name: Optional[str] = None 


# Həm burada {computer_id} olmalıdır
@app.put("/items/{computer_id}") 
async def update_item(
    # Həm də burada computer_id olmalıdır
    computer_id: int = Path(..., title="Kompyuter ID", ge=1, le=1000), 
    computer: Computer = Body(...), 
    user: User = Body(...),
    importance: int = Body(...)
):
    return {"computer_id": computer_id, "computer": computer, "user": user}