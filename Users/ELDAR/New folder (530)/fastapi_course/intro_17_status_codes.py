from fastapi import FastAPI,  status

app = FastAPI()

@app.post("/items/",  status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"message":  "Mehsul yaradildi",  "name": name}


@app.get("/items/",  status_code=200)
async def read_items():
    return [{"name":  "Laptop"},  {"name":  "Mouse"}]


@app.delete("/items/{item_id}",  status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    return None 