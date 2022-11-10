from fastapi import APIRouter
from fastapi import status
from helpers import hash_password, check_password
from schemas.user import CreateUser, UserLogin
from mongoengine import NotUniqueError
from repositories import User
from errors import UserExistedException, UnauthorizedException
from configs import get_config

router = APIRouter(prefix="/users")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: CreateUser):
    try:
        body.password = hash_password(body.password)
        return User.create(body).to_dict()
    except NotUniqueError:
        raise UserExistedException()


@router.post("/login")
async def login(user: UserLogin):
    found_user = User.find_by_username(user.username)
    if (check_password(user.password, found_user.password)):
        return {"api_key": get_config("API_KEY")}
    raise UnauthorizedException("Username or password is incorrect")
    
