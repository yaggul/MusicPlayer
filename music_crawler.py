from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
from mutagen.mp3 import MP3 as mp3
from song import Song

Tk().withdraw()


class MusicCrawler:
    def __init__(self, path_to_songs):
        self.path = path_to_songs
        self.songs = []

    def generate_playlist(self):
        for i in os.listdir(self.path):
            if i.endswith('.mp3'):
                songg = mp3(os.path.realpath(os.path.join(self.path, i)))
                self.songs.append(Song(
                    title=songg['TIT2'][0], artist=songg['TPE1'][0], album=songg[
                        'TALB'][0], length=round(songg.info.length, 2)))
            else:
                pass
        return self.songs
