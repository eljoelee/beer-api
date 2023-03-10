from sqlalchemy import Column, Integer, String

from .database import Base


class Beer(Base):
    __tablename__ = "beers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lat = Column(String, index=True)
    lng = Column(String, index=True)
    address = Column(String, index=True)
    remark = Column(String)
