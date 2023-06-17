class Folder:
    def __init__(self, localFolderName: str):
        self.localFolderName = localFolderName

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)