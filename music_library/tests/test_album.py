from lib.album import Album

"""
Artist constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Title" , 2013 , 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2013
    assert album.artist_id == 1

"""
We can format artists to strings nicely
"""
def test_album_format_nicely():
    album = Album(1, "Test Title" , 2013 , 1)
    assert str(album) == "Artist(1, Test Title, 2013, 1)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Title" , 2013 , 1)
    album2 = Album(1, "Test Title" , 2013 , 1)
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.