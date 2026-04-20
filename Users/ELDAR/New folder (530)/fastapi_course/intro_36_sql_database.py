from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/users/")
def create_user(username: str, email: str, db: Session = Depends(database.get_db)):
    new_user = models.DBUser(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.DBUser).filter(models.DBUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="İstifadəçi tapılmadı")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, new_email: str, db: Session = Depends(database.get_db)):
    user = db.query(models.DBUser).filter(models.DBUser.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        return user
    raise HTTPException(status_code=404, detail="Tapılmadı")

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.DBUser).filter(models.DBUser.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"status": "Silindi"}
    raise HTTPException(status_code=404, detail="Tapılmadı")