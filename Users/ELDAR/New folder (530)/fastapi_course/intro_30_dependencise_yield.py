from fastapi import FastAPI, Depends

app = FastAPI()

async def get_db_session():
    db = "Verilenler Bazasina qosulma yaradildi."
    try:
        print("BAZA: Qosulma acildi")
        yield db
    finally:
        print("BAZA: Qosulma baglandi (Temizlik edildi)")


@app.get("/items/")
async def read_items(db: str = Depends(get_db_session)):
    print(f"ENDPOINT: Bazadan melumatlar oxunur: {db}")
    return {"message":   "Melumatlar geldi."}


