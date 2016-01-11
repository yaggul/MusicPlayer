class Playlist:
    def __init__(self, name=None, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []

    def add_song(self):
        pass

    def remove_song(self):
        pass

    def total_lenght(self):
        pass

    def artists(self):
        pass

    def next_song(self):
        pass

    def pprint_playlist(self):
        pass

    def save(self):
        pass

    @staticmethod
    def load(path):
        pass
