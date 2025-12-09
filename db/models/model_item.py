from pydantic import BaseModel

class ProductsResponse(BaseModel):
    _id: str
    name: str
    price: int
    stock: int
    category: str


class ProductsForm(BaseModel):
    name: str
    price: int
    stock: int
    category: str