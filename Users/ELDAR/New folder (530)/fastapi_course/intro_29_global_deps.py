from fastapi import FastAPI,  Depends, Header, HTTPException

async def verify_global_token(x_token: str = Header(...)):
    if x_token != "global-secret":
        raise HTTPException(status_code=400, detail="Qlobal Token sehvdir.")
    

app = FastAPI(dependencies=[Depends(verify_global_token)])

app.get("/items/")
async def read_items():
    return [{"item":  "Saz"},  {"item":  "Tar"}]

@app.get("/users/")
async def read_users():
    return [{"username":  "Eldar"}]


    