from fastapi import FastAPI, Body 
from pydantic import BaseModel, Field 
from typing import Optional

app = FastAPI()

class Product(BaseModel):
    name: str = Field(..., title="Productun adi",  min_length=2,  max_length=50)
    description: Optional[str] = Field(
        None, title="Tesvir",  max_length=300, description="Mehsul haqqinda tesvir."

    )

    price: float = Field(
        ..., gt=0,  description="Qiymet sifirdan boyuk olmalidir."
    )

    tax: Optional[float] = None 


@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product = Body(..., embed=True)):
    results = {"product_id":  product_id,  "product": product}
    return results


