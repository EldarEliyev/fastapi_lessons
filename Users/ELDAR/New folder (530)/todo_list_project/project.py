from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/tasks/")
def create_task(title: str,  description: str,  db: Session = Depends(database.get_db)):
    new_task = models.TaskDB(title=title,  description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task






@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Not found the task!")
    return task 


@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_title: str, new_description: str, db: Session = Depends(database.get_db)):
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()
    if task:
        task.title = new_title 
        task.description = new_description
        db.commit()
        db.refresh(task)  
        return task
    raise HTTPException(status_code=404, detail="Not found!")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first() # .first() mütləqdir
    if task:
        db.delete(task)
        db.commit()
        return {"status": "Deleted!"}
    raise HTTPException(status_code=404, detail="Not Found!")
