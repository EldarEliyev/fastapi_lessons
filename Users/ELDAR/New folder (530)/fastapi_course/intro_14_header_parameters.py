from fastapi import FastAPI, Header 
from typing import Optional, List

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None),  x_token: Optional[List[str]] = Header(None),  strange_header: Optional[str] = Header(None, convert_underscores=True)):
    return {
        "User-Agent": user_agent,
        "X-Token": x_token,
        "Strange-Header": strange_header

    }