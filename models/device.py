from enum import Enum

from mongoengine import DateTimeField, EnumField, StringField

from helpers import now
from models.basemodel import BaseModel


class DeviceMode(Enum):
    MANUAL = "manual"
    AUTO = "auto"
    SCHEDULE = "schedule"

class DeviceStatus(Enum):
    ON = "on"
    OFF = "off"

class Device(BaseModel):
    name = StringField(max_length=100, required=True)
    mode = EnumField(
        enum=DeviceMode, 
        default="mannual"
    )
    status = EnumField(
        enum=DeviceStatus, 
        default="off"
    )
    created_at = DateTimeField(default=now)
    updated_at = DateTimeField(default=now)
    
    meta = {
        "collection": "devices",
        "indexes": ["#name"]
    }
