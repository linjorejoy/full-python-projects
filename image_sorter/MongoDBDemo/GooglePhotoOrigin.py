from GoogleMobileUpload import GoogleMobileUpload
import mongoengine


class GooglePhotoOrigin(mongoengine.EmbeddedDocument):

    mobileUpload = mongoengine.EmbeddedDocumentField(GoogleMobileUpload)