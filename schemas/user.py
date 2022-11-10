from pydantic import BaseModel


class CreateUser(BaseModel):
    fullname: str
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
