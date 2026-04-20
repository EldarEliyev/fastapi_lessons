from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0,  limit: int = 100):
    return {"q": q,  "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(params: dict = Depends(common_parameters)):
    return {"items":  [{"item_id":  "1"},  {"item_id":  "2"}],  "params": params}

@app.get("/users/")
async def read_users(params: dict = Depends(common_parameters)):
    return {"users":  [{"username":  "eldar"},  {"username":  "aliev"}],  "params": params}


