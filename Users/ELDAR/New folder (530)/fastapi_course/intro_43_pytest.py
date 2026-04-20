from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
async def welcome():
    return {"message":  "Welcome Eldar!"}

@app.get("/sum")
async def calculate_sum(a: int, b: int):
    return {"result":  a + b}

