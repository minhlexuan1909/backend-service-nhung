from mongoengine import DateTimeField, StringField

from helpers import now
from models.basemodel import BaseModel


class Sensor(BaseModel):
    name = StringField(required=True)
    created_at = DateTimeField(default=now)

    meta = {
        'collection': 'sensors',
        'indexes': [
            ('name', 'hashed')
        ]
    }
