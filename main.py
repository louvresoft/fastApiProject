from fastapi import FastAPI
from app.routers import user, auth
from app.db.database import Base, engine


# def create_table():
# Se comenta por configuracion de alembic
#     Base.metadata.create_all(bind=engine)
# create_table()


app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)
