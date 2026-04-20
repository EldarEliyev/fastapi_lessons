from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Şifre initialize sırasında değil, dinamik olarak hash'le
users_db = {
    "eldar2005": {
        "username": "eldar2005",
        "full_name": "Eldar",
        "email": "eldar@example.com",
        "password": "123456",
    }
}

# 3. Login Endpoint (Token almaq üçün)
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_db.get(form_data.username)
    
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="İstifadəçi adı səhvdir"
        )
    
    # Şifrəyi doğru sırada kontrol etme
    password = form_data.password[:72]  # bcrypt 72 byte sınırı
    correct_password = user_dict["password"][:72]
    
    is_correct = password == correct_password
    if not is_correct:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Şifrə səhvdir"
        )

    return {"access_token": "eldar-gizli-token-123", "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"current_token": token, "status": "Giriş uğurludur"}