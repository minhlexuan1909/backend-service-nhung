from mongoengine import DateTimeField, FloatField

from helpers import now
from models.basemodel import BaseModel


class Enviroment(BaseModel):
    humidity = FloatField(required=True, index=True)
    temperature = FloatField(required=True, index=True)
    light = FloatField(required=True, index=True)
    capture_at = DateTimeField(default=now, index=True)

    meta = {
        'collection': 'enviroments'
    }
