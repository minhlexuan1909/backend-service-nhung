import datetime

from mongoengine import DateTimeField, StringField

from models.basemodel import BaseModel


class User(BaseModel):
    fullname = StringField(max_length=50, required=True)
    username = StringField(max_length=200, required=True, unique=True)
    password = StringField(max_length=255, required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'collection': 'users'
    }

    def to_dict(self, *exclude_fields):
        dict_model = super().to_mongo().to_dict()
        dict_model['_id'] = str(dict_model['_id'])
        del dict_model['_cls']
        del dict_model['password']
        
        for field in exclude_fields:
            del dict_model[field]
        return dict_model
    