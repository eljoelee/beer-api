from typing import Optional
from pydantic import BaseModel, Field, BaseConfig


class BeerSchema(BaseModel):
    name: str = Field(title="이름")
    lat: str = Field(title="위도")
    lng: str = Field(title="경도")
    address: str = Field(title="주소")
    remark: Optional[str] = None

    class Config(BaseConfig):
        schema_extra = {
            "example": {
                "name": "테스트",
                "lat": "37.512",
                "lng": "127.109",
                "address": "서울특별시 송파구 오금로15길 11",
                "remark": "테스트입니다."
            }
        }
