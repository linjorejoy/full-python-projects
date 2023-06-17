import json
import mongoengine


class TimeStamp(mongoengine.EmbeddedDocument):
    timestamp = mongoengine.IntField(default=0)
    formatted = mongoengine.StringField()
