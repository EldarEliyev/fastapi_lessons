from fastapi import FastAPI, Cookie 
from typing import Optional


app = FastAPI()

@app.get("/products/")
async def read_items(ads_id: Optional[str] = Cookie(None, title="Reklam ID-si",  description="Istifadecinin izleme kodu")):
    return {"ads_id": ads_id}