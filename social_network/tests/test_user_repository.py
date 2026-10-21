from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    users = repository.all() # Get all artists

    # Assert on the results
    assert users == [
        User(1, 'benny1', 'ben1@mail.se'),
        User(2, 'dallo', 'dalloway@mail.co.uk'),
        User(3, 'emm', 'not3mm@mailmail.com'),
        User(4, 'drac', 'nightowl@hotmail.com'),
        User(5, 'wharty', 'lastone@mail.com')
    ]

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(3)
    assert user == User(3, "emm", "not3mm@mailmail.com")

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "toomster", "dhtoomey@goodwork.mb"))

    result = repository.all()
    assert result == [
        User(1, 'benny1', 'ben1@mail.se'),
        User(2, 'dallo', 'dalloway@mail.co.uk'),
        User(3, 'emm', 'not3mm@mailmail.com'),
        User(4, 'drac', 'nightowl@hotmail.com'),
        User(5, 'wharty', 'lastone@mail.com'),
        User(6, 'toomster', 'dhtoomey@goodwork.mb')
    ]

"""
When we call UserRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        User(1, 'benny1', 'ben1@mail.se'),
        User(2, 'dallo', 'dalloway@mail.co.uk'),
        User(4, 'drac', 'nightowl@hotmail.com'),
        User(5, 'wharty', 'lastone@mail.com'),
    ]
