from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Set


app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str 


class Car(BaseModel):
    brand: str
    model: str 
    description: Optional[str] = None 
    price: int 
    tax: Optional[float] = None 
    tags: List[str] = []
    unique_ids: Set[int] = set()

    image: Optional[Image] = None 

    images: Optional[List[Image]] = None 


@app.put("/cars/{car_id}")
async def update_car(car_id: int, car: Car):
    results = {"car_id": car_id, "car": car}
    return results

