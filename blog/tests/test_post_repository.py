from lib.post import Post
from lib.post_repository import PostRepository
from lib.comment import Comment


#Find a post along with all its comments
def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)
    post = repository.find_with_comments(1)
    assert post == Post(1, 'Neurotoxin Inspection', 'An inspection is due to be carried out today', [
        Comment(1, 'Wheatley', 'begin!', 1),
        Comment(2, 'definitelyNotWheatley', 'Hello Guv. Here are my credentials, shut yourself down', 1),
        Comment(3, 'definitelyNotWheatley', 'I am totally legit, from the board of international, uh, observers, from the UAE', 1),
        Comment(4, 'Chell', '...', 1)
    ])