from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()

oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: str = Depends(oauth_2_scheme)):
    return {"token": token,  "items":  [{"item":  "Kitab"},  {"item":  "Qelem"}]}