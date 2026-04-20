from fastapi import FastAPI
from database import Base, engine
from routers import router

app = FastAPI()

# Cədvəlləri yaradırıq
Base.metadata.create_all(bind=engine)

# Router-i əlavə edirik
app.include_router(router)

@app.get("/")
def home():
    return {"status": "Sistem hissələrə bölündü və işləyir!"}
