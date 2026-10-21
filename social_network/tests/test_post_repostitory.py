from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    posts = repository.all() # Get all artists

    # Assert on the results
    assert posts == [
        Post(1, 'ben is no.1', 'I am the best', 2, 1),
        Post(2, 'retraction', 'I might not be the best', 1, 1),
        Post(3, 'Social media', 'What is with these posts', 22, 3),
        Post(4, 'Night benefits', 'Being awake at night is better', 5, 4),
        Post(5, 'Disappearance?', 'Why has emm not posted', 44, 5)
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, 'Social media', 'What is with these posts', 22, 3)

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")    
    repository = PostRepository(db_connection)

    repository.create(Post(None, "I'm Here", "Don't worry I'm back", 100, 2))

    result = repository.all()
    assert result == [
        Post(1, 'ben is no.1', 'I am the best', 2, 1),
        Post(2, 'retraction', 'I might not be the best', 1, 1),
        Post(3, 'Social media', 'What is with these posts', 22, 3),
        Post(4, 'Night benefits', 'Being awake at night is better', 5, 4),
        Post(5, 'Disappearance?', 'Why has emm not posted', 44, 5),
        Post(6, "I'm Here", "Don't worry I'm back", 100, 2)
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Post(1, 'ben is no.1', 'I am the best', 2, 1),
        Post(2, 'retraction', 'I might not be the best', 1, 1),
        Post(4, 'Night benefits', 'Being awake at night is better', 5, 4),
        Post(5, 'Disappearance?', 'Why has emm not posted', 44, 5)
    ]
