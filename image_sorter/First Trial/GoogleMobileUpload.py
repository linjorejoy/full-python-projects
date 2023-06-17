from Folder import Folder


class GoogleMobileUpload:
    def __init__(self, deviceFolder, deviceType: str):
        self.deviceFolder = Folder(localFolderName=deviceFolder["localFolderName"])
        self.deviceType = deviceType

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)