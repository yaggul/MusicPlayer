# datetime


class Song:
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.artist = kwargs['artist']
        self.album = kwargs['album']
        self.lenght = kwargs['lenght']

    def __str__(self):
        '''
            {artist} - {title} from {album} - {length}
        '''
        return '{{0}} - {{1}} from {{2}} - {{3}}'.format(
            self.title, self.artist, self.album, self.lenght)

    def lenght(self):
        pass
