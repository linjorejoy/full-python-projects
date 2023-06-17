from TimeStamp import TimeStamp
from Location import Location
from GooglePhotoOrigin import GooglePhotoOrigin
from Person import Person
import json
import mongoengine


class GoogleImage(mongoengine.Document):

    title = mongoengine.StringField(required=True)
    description = mongoengine.StringField()
    imageViews = mongoengine.IntField(default=0)
    creationTime = mongoengine.EmbeddedDocumentField(TimeStamp)
    photoTakenTime = mongoengine.EmbeddedDocumentField(TimeStamp)
    geoData = mongoengine.ObjectIdField()
    geoDataExif = mongoengine.ObjectIdField()
    people = mongoengine.ListField()
    googlePhotosOrigin = mongoengine.EmbeddedDocumentField(GooglePhotoOrigin)

    meta = {"db_alias": "core", "collection": "googleimages"}
