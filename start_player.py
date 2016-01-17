# import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
# from mutagen.mp3 import MP3 as mp3
from playlist import Playlist
# from song import Song
from music_crawler import MusicCrawler
Tk().withdraw()


def main():
    path = ''
    while path == '':
        path = askdirectory(title='Please choose path to crawl!')
    crawler = MusicCrawler(path)
    songs = crawler.generate_playlist()
    pname = ''
    print('\n')
    while pname == '':
        pname = input('Please insert playlist name: ')
    playlist = Playlist(pname)
    playlist.add_songs(songs)
    print('\n')
    # print(playlist.playlist1)
    print('\n')
    print(playlist.pprint_playlist())
    print('\n')
    print(playlist.artists())
    print('\n')
    playlist.save()
    playlist.remove_all_songs(playlist.playlist1)
    print(playlist.pprint_playlist())
    print('\n')
    playlist.load(askopenfilename())
    print('\n')
    print(playlist.pprint_playlist())
    print('\n')
    print(playlist.artists())
    print('\n')



if __name__ == '__main__':
    main()
