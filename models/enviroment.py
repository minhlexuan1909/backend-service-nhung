import datetime

from mongoengine import DateTimeField, FloatField

from models.basemodel import BaseModel


class Enviroment(BaseModel):
    humidity = FloatField(required=True, index=True)
    temperature = FloatField(required=True, index=True)
    light = FloatField(required=True, index=True)
    capture_at = DateTimeField(default=datetime.datetime.utcnow, index=True)

    meta = {
        'collection': 'enviroments'
    }
