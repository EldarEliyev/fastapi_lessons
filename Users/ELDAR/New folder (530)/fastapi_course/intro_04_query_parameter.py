from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/items/")
async def read_items(skip: int = 0,  limit: int = 10):
    fake_items_db = [{"item_name": "Book"},  {"item_name": "Television"},  {"item_name":  "Computer"}]
    return fake_items_db[skip: skip + limit]


@app.get("/search/")
async def search_items(q: Optional[str] = None):
    if q:
        return {"axtaris": q,  "netice":  "Melumat tapildi"}
    return {"mesaj":  "Hec bir axtaris parametri daxil edilmeyib"}

