import datetime

from mongoengine import DateTimeField, StringField

from models.basemodel import BaseModel


class Sensor(BaseModel):
    name = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'collection': 'sensors',
        'indexes': [
            ('name', 'hashed')
        ]
    }
