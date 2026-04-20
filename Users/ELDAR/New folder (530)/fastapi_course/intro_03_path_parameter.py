from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "mesaj":  f"Siz {item_id} nomreli mehsula baxirsiniz"}


@app.get("/users/{user_id}/orders/{order_id}")
async def get_user_order(user_id: int, order_id: str):
    return {
        "user_id": user_id,
        "order_id": order_id,
        "info":  "Istifadecinin sifarisi tapildi"
    }

