from fastapi import FastAPI

from sql_app import models
from sql_app.api import menu, submenu
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/api/v1")


app.include_router(menu.router)
app.include_router(submenu.router)
