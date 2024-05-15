import re
from pydantic import BaseModel

class OrderModel(BaseModel):
    number: int
    ingredients: list[str]
    createdAt: str
    name: str
    # price: int
    status: str
    updatedAt: str
