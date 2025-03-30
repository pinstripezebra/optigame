from fastapi import FastAPI
from models import User, Game, Role
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

# database connection string
user_db: List[User] = [
    User(id=UUID("835a05cf-3e31-4b75-977b-6196442d5158"), username="admin", password="admin", role=Role.admin),
    User(id=UUID("e06f8d98-40fe-4447-9983-668d8db5ca6e"), username="user", password="user", role=Role.user)
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return user_db