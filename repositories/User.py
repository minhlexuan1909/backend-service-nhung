from models.user import User
from schemas.user import CreateUser


def create(doc: CreateUser):
    return User(
        fullname=doc.fullname, 
        username=doc.username, 
        password=doc.password
    ).save()


def find_by_username(username: str):
    return User.objects(username=username).only('password').first()
