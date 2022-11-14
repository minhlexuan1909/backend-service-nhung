from typing import Any, Dict

from models.user import User


def create(doc: Dict[str, Any]) -> User:
    return User(**doc).save(force_insert=True)


def find_by_username(username: str) -> User:
    return User.objects(username=username).only('password').first()
