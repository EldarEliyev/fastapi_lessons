from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static",  StaticFiles(directory="static"),  name="static")


@app.get("/get-python-logo")
async def get_logo():
    return {
        "app_name":  "Eldar's  Python App",
        "logo_path": "http://127.0.0.1:8007/static/python_logo.png"    
    }