from Folder import Folder
import mongoengine


class GoogleMobileUpload(mongoengine.EmbeddedDocument):

    deviceFolder = mongoengine.EmbeddedDocumentField(Folder)
    deviceType = mongoengine.StringField(required=True)
