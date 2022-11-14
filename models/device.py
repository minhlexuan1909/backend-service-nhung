from enum import Enum

from mongoengine import DateTimeField, EnumField, StringField, IntField

from helpers import now
from models.basemodel import BaseModel


class DeviceMode(str, Enum):
    MANUAL = "manual"
    AUTO = "auto"
    SCHEDULE = "schedule"


class DeviceStatus(str, Enum):
    ON = "on"
    OFF = "off"


class Device(BaseModel):
    name = StringField(max_length=100, required=True)
    mode = EnumField(
        enum=DeviceMode,
        default=DeviceMode.MANUAL,
        required=True
    )
    status = EnumField(
        enum=DeviceStatus,
        default=DeviceStatus.OFF,
        required=True
    )
    cron = StringField(max_length=50, null=True, default=None)
    duration = IntField(min_value=1, null=True, default=None)
    created_at = DateTimeField(default=now)
    updated_at = DateTimeField(default=now)

    meta = {
        "collection": "devices",
        "indexes": ["#name"]
    }
