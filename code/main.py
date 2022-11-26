from datetime import datetime
from fastapi import FastAPI, Request
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import ENGINE
from model import UserTable, User, InfoTable, Info
from sqlalchemy.orm import sessionmaker
session_factory = sessionmaker(bind=ENGINE)

import os
from fastapi.templating import Jinja2Templates
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory="./templates/WEB")

app = FastAPI()

from pydantic import BaseModel

class json_out(BaseModel):
    id: int
    name: str
    birth: str
    bloodsugar: float
    bloodpressure: float
    ttime: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.get("/c3")
def index(request: Request):
    return templates.TemplateResponse("c3.html", context={"request": request})
    
# ----------API------------
# 테이블에 있는 모든 사용자 정보 GET
@app.get("/users")
def read_users():
    with session_factory() as session:
        users = session.query(UserTable).all()
        return users

# user 특정 정보 GET
@app.get("/usersinfo", response_model=json_out)
def search_user(user_name: str, user_birth: str):
    user_birth = f"{user_birth}T00:00:00"
    with session_factory() as session:
        user = session.query(UserTable).\
            filter(UserTable.name == user_name and UserTable.birth == user_birth).first()

        userinfo = session.query(InfoTable).\
            filter(InfoTable.id == user.id).first()

        print(type(user.birth), type(userinfo.ttime))

        json_ = {'id':user.id, 'name':user.name, 'birth':str(user.birth), 'bloodsugar':userinfo.bloodsugar, 'bloodpressure':userinfo.bloodpressure, 'ttime':str(userinfo.ttime)}
        return json_

# user_id에 해당하는 정보 GET
@app.get("/users/{user_id}")
def read_user(user_id: int):
    with session_factory() as session:
        user = session.query(InfoTable).\
            filter(InfoTable.id == user_id).order_by("ttime").limit(5).all()
        return user

# 사용자 정보 POST
@app.post("/users")
# 쿼리에서 name, birht 받음
# ex) /users?name=Park&birth=2002-05-12
async def create_user(name: str, birth: str):
    with session_factory() as session:
        user = UserTable()
        user.name = name
        user.birth = f"{birth}T00:00:00"
        session.add(user)
        session.commit()

    return f"{name} created..."

@app.post("/userinfo")
async def add_userinfo(id: int, bloodsugar: float, bloodpressure: float):
    with session_factory() as session:
        user = InfoTable()
        user.id = id
        user.bloodsugar = bloodsugar
        user.bloodpressure = bloodpressure
        user.ttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        session.add(user)
        session.commit()

    return f"add userinfo..."

# 복수의 users 정보 갱신 PUT
@app.put("/users")
# model에서 정의한 User 모델의 요청 body를 목록에 넣은 형태로 받기
# ex) users= [{"id": 1, "name": "junseo", "age":20}, {"id":2, "name": "경원", "age":21}]
async def update_users(users: List[User]):
    with session_factory() as session:
        for new_user in users:
            user = session.query(UserTable).filter(UserTable.id == new_user.id).first()
            user.name = new_user.name
            user.birth = new_user.birth
            session.commit()

        return f"{users[0].name} updated..."

@app.put("/userinfomer")
async def update_users(users: List[Info]):
    with session_factory() as session:
        for new_user in users:
            user = session.query(InfoTable).filter(InfoTable.UID == new_user.UID).first()
            user.id = new_user.id
            user.bloodsugar = new_user.bloodsugar
            user.bloodpressure = new_user.bloodpressure
            session.commit()

        return f"{users[0].id} updated..."
        
@app.delete("/users")
async def delete_users(userid: int):
    with session_factory() as session:
        user = session.query(UserTable).filter(UserTable.id == userid).first()
        userinfo = session.query(InfoTable).filter(InfoTable.id == userid).first()
        session.delete(user)
        session.delete(userinfo)
        session.commit()

        return f"User deleted..."
