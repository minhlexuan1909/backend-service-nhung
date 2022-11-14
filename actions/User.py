from mongoengine import NotUniqueError

from configs import get_config
from errors import UnauthorizedException, UserExistedException
from helpers import check_password, hash_password
from repositories import User
from schemas.user import CreateUser, UserLogin


def login(user: UserLogin):
    found_user = User.find_by_username(user.username)

    if (check_password(user.password, found_user["password"])):
        return {"api_key": get_config("API_KEY")}

    raise UnauthorizedException("Username or password is incorrect")


def register(user_info: CreateUser):
    try:
        user_info.password = hash_password(user_info.password)
        return User.create(user_info.dict()).to_dict()
    except NotUniqueError:
        raise UserExistedException()
