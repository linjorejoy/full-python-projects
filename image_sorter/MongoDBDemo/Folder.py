import mongoengine


class Folder(mongoengine.EmbeddedDocument):

    localFolderName = mongoengine.StringField(required=True)
