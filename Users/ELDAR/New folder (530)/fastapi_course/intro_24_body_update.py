from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional


app = FastAPI()

class Item(BaseModel):
    name: str 
    description: Optional[str] = None 
    price: float
    tax: float = 1.5


items = {
    "1":  {"name":  "Laptop",  "description":  "Kohne model",  "price":  1500, "tax": 1.5}
}

@app.put("/items/{item_id}")
async def update_item_put(item_id: str,  item: Item):
    update_item_encoded = item.dict()
    items[item_id] = update_item_encoded
    return update_item_encoded


@app.patch("/items/{item_id}")
async def update_item_patch(item_id: str, item: Item):
    stored_item_data = items.get(item_id)
    if not stored_item_data:
        return {"error":  "Tapilmadi"}

    update_data = item.dict(exclude_unset=True)

    updated_item = {**stored_item_data,  **update_data}
    items[item_id] = updated_item
    return updated_item