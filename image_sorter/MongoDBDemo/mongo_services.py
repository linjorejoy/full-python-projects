import mongoengine
from GoogleImage import GoogleImage
from TimeStamp import TimeStamp
from Location import Location
from Person import Person
from GooglePhotoOrigin import GooglePhotoOrigin
from GoogleMobileUpload import GoogleMobileUpload
from Folder import Folder


def add_image(dictionary: dict) -> GoogleImage:
    image = GoogleImage()
    image.title = dictionary["title"]
    image.description = dictionary["description"]
    image.imageViews = dictionary["imageViews"]

    creationTimeObj = TimeStamp()
    creationTimeObj.timestamp = dictionary["creationTimeObj"]["timestamp"]
    creationTimeObj.formatted = dictionary["creationTimeObj"]["formatted"]
    image.creationTime = creationTimeObj

    photoTakenTimeObj = TimeStamp()
    photoTakenTimeObj.timestamp = dictionary["photoTakenTimeObj"]["timestamp"]
    photoTakenTimeObj.formatted = dictionary["photoTakenTimeObj"]["formatted"]
    image.photoTakenTime = photoTakenTimeObj

    image.geoDataObj = add_Location(dictionary["geoDataObj"])
    image.geoDataExifObj = add_Location(dictionary["geoDataExifObj"])

    image.save()

    for person in dictionary["people"]:
        image.people.append(add_Person(person, image))

    folder = Folder()
    folder.localFolderName = dictionary["googlePhotosOrigin"]["mobileUpload"]["deviceFolder"]["localFolderName"]

    mobileUpload = GoogleMobileUpload()
    mobileUpload.deviceFolder = folder
    mobileUpload.deviceType = dictionary["googlePhotosOrigin"]["mobileUpload"]["deviceType"]

    googlePhotosOrigin = GooglePhotoOrigin()
    googlePhotosOrigin.mobileUpload = mobileUpload

    image.googlePhotosOrigin = googlePhotosOrigin

    image.save()

    return image


def get_Timestamp(dictionary: dict) -> TimeStamp:

    pass


def add_Location(dictionary: dict) -> Location:

    location = Location()
    location.latitude = dictionary["latitude"]
    location.longitude = dictionary["longitude"]
    location.altitude = dictionary["altitude"]
    location.latitudeSpan = dictionary["latitudeSpan"]
    location.longitudeSpan = dictionary["longitudeSpan"]
    # TODO : location.photos

    return location


def add_Person(dictionary: dict, image: GoogleImage) -> Person:
    person = Person()
    person.name = dictionary["name"]
    person.photos.append(image)
    person.folders = []
    person.save()
    # TODO person.photos
    # TODO person.folders
    return person