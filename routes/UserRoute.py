from fastapi import APIRouter, status

from schemas.user import CreateUser, UserLogin
from actions import User

router = APIRouter(prefix="/users")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: CreateUser):
    return User.register(body)


@router.post("/login")
async def login(user: UserLogin):
    return User.login(user)
    