from fastapi import FastAPI, HTTPException, status


app = FastAPI()

items = {"1":  "Bread",  "2":  "Milk"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="Sorry, the id is not found the product.",  headers={"X-Error": "ProductNotFoundError"})
    return {"item_id": items[item_id]}

