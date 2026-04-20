from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Television(BaseModel):
    brand: str = Field(..., examples=["Samsung"])
    model: str = Field(..., examples=["Tv"])
    description: Optional[str] = Field(None, examples=["Televisorun guclu prosessorlari var."])
    price: float = Field(..., examples=[3500.50])

@app.put("/televisions/{television_id}")
async def update_television(television_id: int, television: Television = Body(openapi_examples={"normal":  {"summary":  "Standart melumat",  "description":  "Normal bir televizor numunesi",  "value":  {"brand":  "Samsung",  "price": 5000.50, "description":  "Yaxsi televizor"}}})):
    return {"television_id": television_id,  "television": television}