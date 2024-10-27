from songs import Song
import random

class Playlist:
    def __init__(self, name, repeat = False, shuffle = False):
        self.name = name
        self.songs = []
        self.current_song = 0
        self.repeat = repeat
        self.shuffle = shuffle

    def add_song(self, song):
        if song not in self.songs and isinstance(song, Song):
            self.songs.append(song)
        else:
            print(f"{song} is already added to the playlist")

    def remove_song(self, song):
        if song in self.songs and isinstance(song, Song):
            self.songs.remove(song)
        else:
            print(f"{song} is not there in the playlist")

    def play(self):
        print("My Playlist:")
        if self.shuffle:
            num = random.randint(0, len(self.songs) - 1)
            song = self.songs[num]
            print(song.play())
            self.current_song = num
        if self.repeat:
            print(self.songs[self.current_song].play())
        else:
            song = self.songs[self.current_song]
            print(song.play())

    def skip(self):
        next_song = self.current_song + 1
        if next_song < len(self.songs):
            self.current_song = next_song

    def previous_track(self):
        previous_song = self.current_song - 1
        if previous_song > 0:
            self.current_song = previous_song

playlist = Playlist("My Playlist", repeat=True, shuffle=False)
playlist.add_song(Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", "3:54", "Rock"))
playlist.add_song(Song("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", "8:02", "Rock"))
playlist.skip()
playlist.play()