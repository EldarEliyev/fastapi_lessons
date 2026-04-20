from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str 
    description: str 
    task_count: int 


class TaskCreate(TaskBase):
    pass 


class TaskOut(TaskBase):
    task_id: int 

    class Config:
        from_attributes = True 