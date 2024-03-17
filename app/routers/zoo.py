from fastapi import APIRouter, Query, Path, Depends, HTTPException
from .. import crud, schemas
from ..dependencies import get_db
from typing import Annotated
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/zoo",
    tags=["zoo"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.Zoo])
def read_all_zoo(db: Session = Depends(get_db)):
    return crud.get_all_zoo(db)


@router.get("/{zoo_id}", response_model=list[schemas.Zoo])
def read_zoo(zoo_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    db_zoo = crud.get_zoo(db, zoo_id)
    if db_zoo == None:
        raise HTTPException(status_code=404, detail="Zoo not found")
    return db_zoo


@router.post("/", response_model=schemas.Zoo, status_code=201)
def create_zoo(zoo: schemas.ZooCreate, db: Session = Depends(get_db)):
    db_zoo = crud.get_zoo_by_name(db, zoo.name)
    if db_zoo:
        raise HTTPException(status_code=400, detail="Zoo already exists")
    return crud.create_zoo(db, zoo)


@router.get("/{zoo_id}", response_model=schemas.Zoo)
def read_zoo(zoo_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    deleted_zoo = crud.delete_zoo(db, zoo_id)
    if deleted_zoo == None:
        raise HTTPException(status_code=404, detail="Zoo not found")
    return deleted_zoo