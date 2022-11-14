from mongoengine import Document


class BaseModel(Document):
    meta = {
        'abstract': True,
    }

    def to_dict(self, exclude_fields=[]):
        dict_model = super().to_mongo().to_dict()
        dict_model['_id'] = str(dict_model['_id'])
        dict_model.pop('_cls', None)

        for field in ['_cls'] + exclude_fields:
            dict_model.pop(field, None)

        return dict_model
