from fastapi import APIRouter, Request, status, Body
from fastapi.encoders import jsonable_encoder
from typing import List
from server.model import BeerSchema

router = APIRouter()


@router.put("/", response_description="Create a new Beer", status_code=status.HTTP_201_CREATED, response_model=BeerSchema)
def create_beer(request: Request, beer: BeerSchema = Body(...)):
    beer = jsonable_encoder(beer)
    new_beer = request.app.db["Maps"].insert_one(beer)
    created_beer = request.app.db["Maps"].find_one(
        {"_id": new_beer.inserted_id}
    )

    return created_beer


@router.get("/", response_description="List all Beers", response_model=List[BeerSchema])
def list_beers(request: Request):
    beers = list(request.app.db["Maps"].find())
    return beers
