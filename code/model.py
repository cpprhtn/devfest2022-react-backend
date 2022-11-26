from datetime import datetime
from sqlite3 import Timestamp
from sqlalchemy import Column, Integer, String, Float, DateTime, TIMESTAMP
from pydantic import BaseModel
from db import Base
from db import ENGINE


# user 테이블 정의
class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    birth = Column(String(20), nullable=False)

class InfoTable(Base):
    __tablename__ = 'userinfo'
    id = Column(Integer)
    bloodsugar = Column(Float)
    bloodpressure = Column(Float)
    ttime = Column(TIMESTAMP)
    UID = Column(Integer, primary_key=True, autoincrement=True)

# POST나 PUT때 받는 Request Body 모델 정의
class User(BaseModel):
    id: int
    name: str
    birth: str

class Info(BaseModel):
    id: int
    bloodsugar: float
    bloodpressure: float
    ttime: Timestamp
    UID: int

def main():
    #테이블이 없으면 테이블 생성
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
