import datetime
from enum import Enum

from mongoengine import DateTimeField, EnumField, StringField

from models.basemodel import BaseModel


class DeviceMode(Enum):
    MANUAL = 'manual'
    AUTO = 'auto'
    SCHEDULE = 'schedule'

class DeviceStatus(Enum):
    ON = 'on'
    OFF = 'off'

class Device(BaseModel):
    name = StringField(max_length=100, required=True)
    mode = EnumField(
        enum=DeviceMode, 
        default='mannual'
    )
    status = EnumField(
        enum=DeviceStatus, 
        default='off'
    )
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)
    
    meta = {
        'collection': 'devices',
        'indexes': [
            ('name', 'hashed')
        ]
    }
