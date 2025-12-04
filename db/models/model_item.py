from pydantic import BaseModel

class Item(BaseModel):
    _id: str
    name: str
    price: str
    amount: str
    category: str
