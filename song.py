import time
# lenght = 268.9567083333333


class Song:
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.artist = kwargs['artist']
        self.album = kwargs['album']
        self.length = kwargs['length']
        self.path = kwargs['filename']

    def __str__(self):
        '''
            {artist} - {title} from {album} - {length}
        '''
        return '{{0}} - {{1}} from {{2}} - {{3}}'.format(
            self.title, self.artist, self.album, self.length)

    def get_length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.length
        elif minutes:
            return int(time.strftime('%M', time.gmtime(self.length)))
        elif hours:
            return int(time.strftime('%H', time.gmtime(self.length)))
        else:
            if self.length >= 3600:
                return time.strftime('%H:%M:%S', time.gmtime(self.length))
            else:
                return time.strftime('%M:%S', time.gmtime(self.length))

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def __repr__(self):
        return 'Song(title="{}", artist="{}", album="{}", length={}, filename="{}")'.format(
            self.title, self.artist, self.album, self.length, self.path)
