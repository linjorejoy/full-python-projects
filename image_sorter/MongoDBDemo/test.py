import mongoengine
import json
import mongo_services as svc
import mongo_setup as mongo_setup


mongo_setup.global_init()
obj_str = """{
    "title": "IMG_20191228_143958.jpg",
    "description": "",
    "imageViews": "0",
    "creationTimeObj": {
        "timestamp": "1577866225",
        "formatted": ""
    },
    "photoTakenTimeObj": {
        "timestamp": "1577524198",
        "formatted": ""
    },
    "geoDataObj": {
        "latitude": 9.483658388888887,
        "longitude": 76.61004127777777,
        "altitude": 0.0,
        "latitudeSpan": 0.0,
        "longitudeSpan": 0.0
    },
    "geoDataExifObj": {
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
}"""


json_dict = json.loads(obj_str)

# print(json_dict)

svc.add_image(json_dict)