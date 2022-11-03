from passlib.hash import bcrypt
from typing import List

def hash_password(plain: str):
    return bcrypt.hash(plain)

def check_password(plain: str, hashed: str):
    return bcrypt.verify(plain, hashed)
