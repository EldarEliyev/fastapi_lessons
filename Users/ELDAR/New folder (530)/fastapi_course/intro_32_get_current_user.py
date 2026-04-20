from fastapi import Depends,  FastAPI,  HTTPException,  status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str 
    email: str | None = None 
    full_name: str | None = None 

fake_users_db = {
    "eldar2005": {
        "username": "eldar2005",
        "full_name": "Eldar Eliyev",
        "email":  "eldar@example.com"
    }
}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user_dict = fake_users_db.get("eldar2005")

    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Istifadeci tapilmadi."
        )
    
    return User(**user_dict)


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user