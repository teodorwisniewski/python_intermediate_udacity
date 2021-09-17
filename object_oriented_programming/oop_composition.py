""""
Exercise 1
Briefly describe a possible collection of classes which can be used to represent a music collection
(for example, inside a music player), focusing on how they would be related by composition.
You should include classes for songs, artists, albums and playlists.
Hint: write down the four class names, draw a line between each pair of classes which you think should have a relationship,
and decide what kind of relationship would be the most appropriate.

For simplicity you can assume that any song or album has a single “artist” value (which could represent more than one person),
but you should include compilation albums (which contain songs by a selection of different artists).
The “artist” of a compilation album can be a special value like “Various Artists”.
You can also assume that each song is associated with a single album,
but that multiple copies of the same song (which are included in different albums) can exist.

Write a simple implementation of this model which clearly shows how the different classes are composed.
Write some example code to show how you would use your classes to create an album and add all its songs to a playlist.
Hint: if two objects are related to each other bidirectionally,
you will have to decide how this link should be formed – one of the objects will have to be created before the other,
so you can’t link them to each other in both directions simultaneously!

"""

class Song:

    def __init__(self,name, artist, album):
        self.name = name
        self.artist = artist
        self.album = album
        artist.add_song(self)

    def __str__(self):
        return f"title: \"{self.name}\", artist: {self.artist.name}, album: {self.album.name } \n"

    def __repr__(self):
        return f"title: \"{self.name}\", artist: {self.artist.name}, album: {self.album.name } \n"

class Album:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year
        self.songs = []

    def add_song(self, song_name):
        new_song = Song(song_name, self.artist, self)
        self.songs.append(new_song)
        return new_song

    def __str__(self):
        songs = "->".join([
            f"{i+1}. {song}"
            for i, song in enumerate(self.songs)
        ])
        return f"Artist: {self.artist.name}\n" \
               f"Album name: {self.name}\n" \
               f"Released data: {self.year}\n" \
               f"list of songs:\n->{songs}"

class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, name, year):
        album = Album(name, self, year)
        self.albums.append(album)
        return album

    def add_song(self, song):
        self.songs.append(song)




class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        songs = "->".join([
            f"{i+1}. {song}"
            for i, song in enumerate(self.songs)
        ])
        return f"Playlist name: {self.name}\n" \
               f"list of songs:\n->{songs}"


if __name__ == "__main__":
    artist_eminem = Artist("Eminem")
    album_recovery = artist_eminem.add_album("Recovery", 2010)
    song1 = album_recovery.add_song("Cold Wind Blows")
    song2 = album_recovery.add_song("Talkin' 2 Myself")
    song3 = album_recovery.add_song("On Fire")
    song4 = album_recovery.add_song("W.T.P")
    song5 = album_recovery.add_song("Going Through Changes")

    print(album_recovery)


    album_relapse = artist_eminem.add_album("Relapse", 2009)
    song6 = album_relapse.add_song("Forever")
    song7 = album_relapse.add_song("Hell Breaks Loose")
    song8 = album_relapse.add_song("Buffalo Bill")
    song9 = album_relapse.add_song("Elevator")
    song10 = album_relapse.add_song("Taking My Ball")

    print(album_relapse)

    songs = artist_eminem.songs
    print(songs)


    band = Artist("Bob's Awesome Band")
    album = Album("Bob's First Single", band, 2013)
    album.add_song("A Ballad about Cheese")
    album.add_song("A Ballad about Cheese (dance remix)")
    album.add_song("A Third Song to Use Up the Rest of the Space")

    playlist = Playlist("My Favourite Songs")

    for song in album.songs:
        playlist.add_song(song)

    print(playlist)