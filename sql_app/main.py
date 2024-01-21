from fastapi import FastAPI


from sql_app.api import menu
from sql_app import models
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_prefix="/api/v1")


app.include_router(menu.router)
