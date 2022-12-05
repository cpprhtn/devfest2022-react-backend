from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db import ENGINE
from model import ProductInfo, UserInfo
from sqlalchemy.orm import sessionmaker
session_factory = sessionmaker(bind=ENGINE)

app = FastAPI()

from pydantic import BaseModel

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def rm(prod, user_id):
    if user_id == 0:
        del prod[0]
        del prod[0]
        del prod[0]
    elif user_id == 1:
        del prod[3]
        del prod[3]
        del prod[8]
    elif user_id == 2:
        del prod[5]
        del prod[6]
        del prod[6]
    else:
        del prod[6]
        del prod[8]
        del prod[8]
    return prod

# ----------API------------
# 테이블에 있는 모든 사용자 정보 GET
@app.get("/product")
def read_users():
    with session_factory() as session:
        prod = session.query(ProductInfo.id, ProductInfo.name, ProductInfo.price, ProductInfo.category, ProductInfo.chats, ProductInfo.views, ProductInfo.userID, ProductInfo.img, ProductInfo.dates, ProductInfo.info, ProductInfo.favorites, UserInfo.location).join(UserInfo, ProductInfo.userID == UserInfo.userID).all()
        return prod

@app.get("/product/{product_id}")
def read_users(product_id: int):
    with session_factory() as session:
        prod = session.query(ProductInfo).\
            filter(ProductInfo.id == product_id).all()
        user = session.query(UserInfo).\
            filter(UserInfo.userID == prod[0].userID).all()
        prod[0].location = user[0].location
        return prod[0]

@app.get("/users/{user_id}")
def read_user(user_id: int):
    with session_factory() as session:
        user = session.query(UserInfo).\
            filter(UserInfo.userID == user_id).all()
        prod = session.query(ProductInfo.name, ProductInfo.img, ProductInfo.price).all()
        prod = rm(prod, user_id)
        user[0].other = prod
        return user[0]