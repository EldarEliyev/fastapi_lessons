from datetime import datetime 
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel 


app = FastAPI()

class Food(BaseModel):
    name: str 
    price: float 
    description: str | None = None 

fake_db = {}


@app.put("/foods/{food_id}")
def update_food(food_id: str, food: Food):
    json_compatible_food_data = jsonable_encoder(food)
    fake_db[food_id] = jsonable_encoder(food)
    return {"message": "Uğurla yeniləndi", "data": json_compatible_food_data}