import json


class TimeStamp:
    def __init__(self, timestamp: int, formatted: str):
        self.timestamp = timestamp
        self.formatted = ""

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
