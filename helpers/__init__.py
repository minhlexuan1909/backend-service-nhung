import datetime as dt
from typing import Any, Dict, Union

from croniter import croniter
from passlib.hash import bcrypt


def hash_password(plain: str):
    return bcrypt.hash(plain)


def check_password(plain: str, hashed: str):
    return bcrypt.verify(plain, hashed)


def now():
    return dt.datetime.utcnow()


def parse_enviroment_capture(raw: str) -> Dict[str, float]:
    enviroment: Dict[str, float] = {}

    features = raw.split("|")

    for feature in features:
        [key, value] = feature.split("=")
        value = float(value)
        enviroment[key] = value

    return enviroment


def generate_mqtt_payload(data: Dict[str, Any]) -> str:
    features = []
    for [key, value] in data.items():
        features.append(f"{key}={value}")
    return "|".join(features)


def is_valid_cron(cron: Union[None, str]):
    return False if cron == None else croniter.is_valid(cron)
