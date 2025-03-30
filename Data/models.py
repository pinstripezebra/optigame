from pydantic import BaseModel
from uuid import UUID,uuid4
from typing import Optional
from enum import Enum
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

# Initialize the base class for SQLAlchemy models
Base = declarative_base()

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    username: str
    password: str
    role: Role


class Game(Base):
    __tablename__ = "optigame_products"  # Table name in the PostgreSQL database

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4(), unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)
    sales_volume = Column(Integer, nullable=True)
    reviews_count = Column(Integer, nullable=True)
    asin = Column(String, unique=True, nullable=False)