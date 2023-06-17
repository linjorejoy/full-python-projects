class Location:
    def __init__(self, latitude: float, longitude: float, altitude: float, latitudeSpan: float, longitudeSpan: float):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.latitudeSpan = latitudeSpan
        self.longitudeSpan = longitudeSpan

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)