from TimeStamp import TimeStamp
from Location import Location
from GooglePhotoOrigin import GooglePhotosOrigin
import json


class GoogleImage:
    def __init__(
        self,
        title,
        description,
        imageViews,
        creationTime,
        photoTakenTime,
        geoData,
        geoDataExif,
        people,
        googlePhotosOrigin,
    ):
        self.title = title
        self.description = description
        self.imageViews = imageViews
        self.creationTimeObj = TimeStamp(creationTime["timestamp"], creationTime["formatted"])
        self.photoTakenTimeObj = TimeStamp(photoTakenTime["timestamp"], photoTakenTime["formatted"])
        self.geoDataObj = Location(
            geoData["latitude"],
            geoData["longitude"],
            geoData["altitude"],
            geoData["latitudeSpan"],
            geoData["longitudeSpan"],
        )
        self.geoDataExifObj = Location(
            geoDataExif["latitude"],
            geoDataExif["longitude"],
            geoDataExif["altitude"],
            geoDataExif["latitudeSpan"],
            geoDataExif["longitudeSpan"],
        )
        self.people = []
        self.googlePhotosOrigin = GooglePhotosOrigin(mobileUpload=googlePhotosOrigin["mobileUpload"])

    @classmethod
    def from_json(cls, json_dict: dict):
        return cls(**json_dict)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


if __name__ == "__main__":

    json_str = """{
    "title": "IMG_20191228_143958.jpg",
    "description": "",
    "imageViews": "0",
    "creationTime": {
        "timestamp": "1577866225",
        "formatted": "Jan 1, 2020, 8:10:25 AM UTC"
    },
    "photoTakenTime": {
        "timestamp": "1577524198",
        "formatted": "Dec 28, 2019, 9:09:58 AM UTC"
    },
    "geoData": {
        "latitude": 9.483658388888887,
        "longitude": 76.61004127777777,
        "altitude": 0.0,
        "latitudeSpan": 0.0,
        "longitudeSpan": 0.0
    },
    "geoDataExif": {
        "latitude": 9.483658388888887,
        "longitude": 76.61004127777777,
        "altitude": 0.0,
        "latitudeSpan": 0.0,
        "longitudeSpan": 0.0
    },
    "people": [
        {
        "name": "Linjo"
        },
        {
        "name": "Alby"
        },
        {
        "name": "Ally"
        },
        {
        "name": "Linto"
        }
    ],
    "googlePhotosOrigin": {
        "mobileUpload": {
        "deviceFolder": {
            "localFolderName": ""
        },
        "deviceType": "ANDROID_PHONE"
        }
    }
    }
    """

    im = GoogleImage.from_json(json_str)
    dictionary = im.toJSON()
    print("\n" * 2)
    print(dictionary)
    print("\n" * 2)
