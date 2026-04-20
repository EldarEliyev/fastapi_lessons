from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,  OAuth2PasswordRequestForm
from typing import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "me":  "Istifadeci melumatlarini oxumaq icazesi",
        "items":  "Mehsullara baxmaq ve redakte etmek icazesi"
    }
)


@app.post("/token")
async def login(form_data:  Annotated[OAuth2PasswordRequestForm,  Depends()]):
    return {
        "accesss_token":  f"{form_data.username}_token_with_scopes",
        "token_type":  "bearer",
        "scopes":  form_data.scopes
    }

@app.get("/users/me")
async def read_users_me(token: Annotated[str,  Depends(oauth2_scheme)]):
    return {
        "user":  "eldar2005",
        "active_scopes":  "Senin 'me' icazen tesdiqlendi"
    }