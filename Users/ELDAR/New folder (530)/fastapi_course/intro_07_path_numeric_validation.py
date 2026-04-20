from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: int = Path(..., title="Productun ID-si",  ge=1,  le=1000), q: Optional[str] = Query(None, alias="item-query")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/products/{product_id}")
async def get_product(product_id: int = Path(..., gt=0, lt=100), size: float = Query(..., gt=0, lt=10.5)):
    return {"product_id": product_id, "size": size}

