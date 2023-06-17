from GoogleMobileUpload import GoogleMobileUpload


class GooglePhotosOrigin:
    def __init__(self, mobileUpload):
        self.mobileUpload = GoogleMobileUpload(
            deviceFolder=mobileUpload["deviceFolder"], deviceType=mobileUpload["deviceType"]
        )

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)