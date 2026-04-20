from fastapi import FastAPI,  Query 
from typing import Optional

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, pattern="^fixedquery$",  title="Search text",  description="Enter text here for find the products")):
    results = {"items":  [{"item_id":  "Portagal"},  {"item_id":  "Gul"}]}
    if q:
        results.update({"q": q})
    return results 

@app.get("/items_list/")
async def read_items_list(q: list[str] = Query(["default_1",  "default_2"])):
    return {"q": q}

