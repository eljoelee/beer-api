from sqlalchemy.orm import Session
from . import models, schemas


def get_beer(db: Session, beer_id: int):
    return db.query(models.Beer).filter(models.Beer.id == beer_id).first()


def get_beers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Beer).offset(skip).limit(limit).all()


def create_beer(db: Session, beer: schemas.BeerCreate):
    db_beer = models.Beer(**beer.dict())
    db.add(db_beer)
    db.commit()
    db.refresh(db_beer)

    return db_beer
