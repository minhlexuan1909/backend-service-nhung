from typing import Any


class __Cache:
    def __init__(self) -> None:
        self.__cache = {}

    def get(self, key: str, default=None) -> Any:
        return self.__cache.get(key, default)

    def set(self, key: str, value: Any):
        self.__cache[key] = value

CACHE = __Cache()
