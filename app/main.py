from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .routers import animals, employees, illness_dairy, zoo

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(zoo.router)
# app.include_router(employees.router)
# app.include_router(illness_dairy.router)
# app.include_router(animals.router)


@app.get("/")
async def root():
    return {"message": "FastAPI app example"}