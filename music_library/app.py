from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):
        # Connect to the database
        self.connection = DatabaseConnection()
        self.connection.connect()
        # Seed with some seed data
        self.connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager")
        print("\n")
        print("What would you like to do?")
        print(" 1 - List all albums")
        print(" 2 - List all artists")
        print("\n")
        num = input("Enter your choice: ")
        print("\n")

        if num == "1":
            album_repository = AlbumRepository(self.connection)
            albums = album_repository.all()
            print("Here is the list of albums:")
            for album in albums:
                print(f" * {album.id} - {album.title}")
        elif num == "2":
            artist_repository = ArtistRepository(self.connection)
            artists = artist_repository.all()
            print("Here is the list of artists:")
            for artist in artists:
                print(f" * {artist.id} - {artist.name} ({artist.genre})")



if __name__ == '__main__':
    app = Application()
    app.run()


# Retrieve all artists
#artist_repository = ArtistRepository(connection)
#artists = artist_repository.all()

# List them out
#for artist in artists:
#    print(artist)

#album_repository = AlbumRepository(connection)
#albums = album_repository.all()

#for album in albums:
#    print(album)

#print(album_repository.find(1))