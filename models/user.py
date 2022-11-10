from helpers import now

from mongoengine import DateTimeField, StringField

from models.basemodel import BaseModel


class User(BaseModel):
    fullname = StringField(max_length=50, required=True)
    username = StringField(max_length=200, required=True, unique=True)
    password = StringField(max_length=255, required=True)
    created_at = DateTimeField(default=now)
    updated_at = DateTimeField(default=now)

    meta = {
        'collection': 'users'
    }

    def to_dict(self, exclude_fields=[]):
        return super().to_dict(exclude_fields + ['password'])
            