import mongoengine


class Location(mongoengine.Document):

    latitude = mongoengine.FloatField(default=0.0)
    longitude = mongoengine.FloatField(default=0.0)
    altitude = mongoengine.FloatField(default=0.0)
    longitudeSpan = mongoengine.FloatField(default=0.0)
    latitudeSpan = mongoengine.FloatField(default=0.0)
    photos = mongoengine.ListField()

    meta = {"db_alias": "core", "collection": "locations"}