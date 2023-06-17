class Image:
    def __init__(self, path: str):

        self.id = None
        self.path = path
        self.timestamp = None
        self.albums = []
        self.tags = []
