from fastapi import FastAPI
from database import models, db_setup
from routers import user_routes


app = FastAPI()

models.Base.metadata.create_all(bind=db_setup.engine)

app.include_router(user_routes.router)