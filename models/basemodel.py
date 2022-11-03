from mongoengine import Document


class BaseModel(Document):
    meta = {
        'abstract': True,
    }

    def to_dict(self, *exclude_fields):
        dict_model = super().to_mongo().to_dict()
        dict_model['_id'] = str(dict_model['_id'])
        del dict_model['_cls']
        
        for field in exclude_fields:
            del dict_model[field]
        return dict_model
