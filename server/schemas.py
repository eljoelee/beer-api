from typing import Optional
from pydantic import BaseModel


class BeerBase(BaseModel):
    name: str
    lat: str
    lng: str
    address: str
    remark: Optional[str] = None


class BeerCreate(BeerBase):
    pass


class Beer(BeerBase):
    id: int

    class Config:
        orm_mode = True
