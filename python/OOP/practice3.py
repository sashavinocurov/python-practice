class Song:
   
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

#help(Song.__init__)
print(Song.__doc__)
print(Song.__init__,__doc__)
