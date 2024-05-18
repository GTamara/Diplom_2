from pydantic import BaseModel

class OrderModel(BaseModel):
    number: int
    ingredients: list[str]
    createdAt: str
    name: str
    status: str
    updatedAt: str
