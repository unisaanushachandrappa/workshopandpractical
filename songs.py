class Song:
    def __init__(self, title, artist, album, duration, genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.genre = genre

    def play(self):
        #//return f"{self.title}\n{self.artist}--{self.album}...\n{self.duration}"
        return f"{self.title} by {self.artist} from {self.album}"