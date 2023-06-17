import mongoengine


class Person(mongoengine.Document):

    name = mongoengine.StringField(required=True)
    photos = mongoengine.ListField()
    folders = mongoengine.ListField()

    meta = {"db_alias": "core", "collection": "people"}
