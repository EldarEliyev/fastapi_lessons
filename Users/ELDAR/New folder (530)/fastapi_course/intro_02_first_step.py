from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status":  "Ugurlu",  "mesaj":  "Ilk FastAPI tetbiqi isleyir!"}


@app.get("/test")
async def test_page():
    return {"sahife":  "Bu test sehifesidir."}

