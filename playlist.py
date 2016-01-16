import time
import json
from song import Song
from prettytable import PrettyTable as pt


class Playlist:

    @staticmethod
    def load_from_json(path):
        with open(path, 'r') as playlistin:
            data = json.load(playlistin)
        return data

    @staticmethod
    def save_to_json(path, playlist):
        playlist = {'Songs': playlist}
        with open(path, 'w') as playlistout:
            json.dump(playlist, playlistout, indent=4)

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist1 = []
        self.shuffled = []
        self.song_index = 0

    def __repr__(self):
        return 'Playlist(name={}, repeat={}, shuffle={}, songs={}'.format(
            self.name, self.repeat, self.shuffle, self.playlist1)

    def add_song(self, song):
        self.playlist1.append(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def remove_song(self, song):
        self.playlist1.remove(song)

    def total_lenght(self):
        total_lenght = sum([song.get_length(seconds=True) for song in self.playlist1])
        return time.strftime('%H:%M:%S', time.gmtime(total_lenght))

    def artists(self):
        hist_str = ''
        artist_hist = {x.artist: [y.artist for y in self.playlist1].count(x.artist) for x in self.playlist1}
        for k, v in artist_hist.items():
            hist_str += '{} : \t{}\n'.format(k, v)
        return hist_str

    def next_song(self):
        song = self.playlist1[self.song_index]
        self.song_index += 1
        return song

    def pprint_playlist(self):
        songs_tbl = pt(['Artist', 'Song', 'Length'])
        songs_tbl.align['Artist'] = 'l'
        songs_tbl.align['Song'] = 'l'
        for i in self.playlist1:
            row = [i.get_artist(), i.get_title(), i.get_length()]
            songs_tbl.add_row(row)
        songs_tbl.add_row(['', '', ''])
        songs_tbl.add_row(['', '', ''])
        songs_tbl.add_row(['', '---------------------', '------------'])
        songs_tbl.add_row(['', 'Total Playlist Length', self.total_lenght()])
        return str(songs_tbl)

    def save(self):
        Playlist.save_to_json('./playlist.json', self.playlist1)

    def load(self, path):
        data = Playlist.load_from_json(path)
        for i in range(len(data['Songs'])):
            self.playlist1[i] = eval(data['Songs'][i])
