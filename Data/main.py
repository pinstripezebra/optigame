from fastapi import FastAPI, Depends
from Data.models import User, Game, Role
from typing import List
from uuid import uuid4, UUID
import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv



# database connection string
user_db: List[User] = [
    User(id=UUID("835a05cf-3e31-4b75-977b-6196442d5158"), username="admin", password="admin", role=Role.admin),
    User(id=UUID("e06f8d98-40fe-4447-9983-668d8db5ca6e"), username="user", password="user", role=Role.user)
]
# Load environment variables from .env2 file
load_dotenv(dotenv_path=".env2")

# Load the database connection string from the environment variable
DATABASE_URL = os.environ.get("POST_DB_LINK")
print(DATABASE_URL)
# Initialize the database connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create the database tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the FastAPI app
app = FastAPI(title="Game Store API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return user_db

@app.get("/api/v1/products")
async def fetch_products(db: Session = Depends(get_db)):
    # Query the "optigame_products" table
    products = db.query(Game).all()
    return products