from datetime import datetime, timedelta
from jose import jwt 
from fastapi import FastAPI, Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# Şifrələri yoxlamaq üçün əlavə:
from passlib.context import CryptContext

app = FastAPI()

# --- Şifrələmə üçün mühit (Argon2 istifadə edir - Python 3.13 ilə uyumlu) ---
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# --- İstifadəçi Bazası (Users DB) ---
users_db = {
    "eldar2005": {
        "username": "eldar2005",
        "hashed_password": pwd_context.hash("123456"), # '123456' şifrəsi Argon2 ilə hash olunub
    }
}

SECRET_KEY = "eldar_cox_gizli_acar_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. İstifadəçini bazadan tapırıq
    user = users_db.get(form_data.username)
    
    # 2. Yoxlama məntiqi:
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="İstifadəçi adı və ya şifrə səhvdir",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    return {"message": "Sen heqiqi JWT token istifade edirsen!", "token_data": token}