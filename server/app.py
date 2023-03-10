from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.Beer])
def read_beers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    beers = crud.get_beers(db, skip=skip, limit=limit)
    return beers


@app.get("/{beer_id}", response_model=schemas.Beer)
def read_beer(beer_id: int, db: Session = Depends(get_db)):
    db_beer = crud.get_beer(db, beer_id=beer_id)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return db_beer


@app.post("/", response_model=schemas.Beer)
def create_beer(beer: schemas.BeerCreate, db: Session = Depends(get_db)):
    return crud.create_beer(db=db, beer=beer)
