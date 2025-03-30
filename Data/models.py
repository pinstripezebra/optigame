from pydantic import BaseModel
from uuid import UUID,UUID4
from typing import Optional
from enum import Enum

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class User(BaseModel):
    id: Optional[UUID] = UUID4
    username: str
    password: str
    role: Role


class Game(BaseModel):
    id: Optional[UUID] = UUID4
    title: str
    description: str
    price: float
    rating: float
    sales_volume: int
    reviews_count: int
    asin: str