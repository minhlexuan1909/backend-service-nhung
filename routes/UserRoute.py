from fastapi import APIRouter, status, HTTPException
from fastapi import status
from helpers import hash_password, check_password
from schemas.user import CreateUser
from mongoengine import NotUniqueError
from repositories import User

router = APIRouter(prefix="/users")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: CreateUser):
    try:
        body.password = hash_password(body.password)
        return User.create(body).to_dict()
    except NotUniqueError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username has already existed"
        )


@router.post("/login")
async def login():
    return {"message": "OK"}
