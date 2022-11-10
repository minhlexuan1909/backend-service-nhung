import datetime as dt
from enum import Enum
from typing import List

from passlib.hash import bcrypt


def hash_password(plain: str):
    return bcrypt.hash(plain)


def check_password(plain: str, hashed: str):
    return bcrypt.verify(plain, hashed)


def now():
    return dt.datetime.utcnow()
