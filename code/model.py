from datetime import datetime
from sqlite3 import Date as Dates
from sqlalchemy import Column, Integer, String, Float, DateTime, TIMESTAMP, Date, types
from pydantic import BaseModel
from db import Base
from db import ENGINE
# user 테이블 정의
class ProductInfo(Base):
    __tablename__ = 'productinfo'
    id = Column(Integer, primary_key=True)
    userID = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    img = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    dates = Column(Date)
    category = Column(String(30), nullable=False)
    info = Column(String(500), nullable=False)
    chats = Column(Integer, nullable=False)
    favorites = Column(Integer, nullable=False)
    views = Column(Integer, nullable=False)


class UserInfo(Base):
    __tablename__ = 'userinfo'
    userID = Column(Integer, primary_key=True)
    profileImg = Column(String(200), nullable=False)
    userName = Column(String(30), nullable=False)
    location = Column(String(30), nullable=False)
    rating = Column(Float, nullable=False)


# POST나 PUT때 받는 Request Body 모델 정의
class Product(BaseModel):
    id: int
    userID: int
    name: str
    img: str
    price: float
    dates: Dates
    category: str
    info: str
    chats: int
    favorites: int
    views: int


class User(BaseModel):
    userID: int
    profileImg: str
    userName: str
    location: str
    rating: float
    
def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
