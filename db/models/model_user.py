from pydantic import BaseModel

class UserDB(BaseModel):
    _id: str
    name: str
    email: str
    password: str
    type: str

class UserForm(BaseModel):
    name: str
    email: str
    password: str
    type: str