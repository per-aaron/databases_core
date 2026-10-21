from lib.post import Post

"""
Post constructs with an id, name and genre
"""
def test_post_constructs():
    post = Post(1, "Test title", "Test content", 0, 2)
    assert post.id == 1
    assert post.title == "Test title"
    assert post.content == "Test content"
    assert post.views == 0
    assert post.user_id == 2

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Test title", "Test content", 0, 2)
    assert str(post) == "Post(1, Test title, Test content, 0, 2)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test title", "Test content", 0, 2)
    post2 = Post(1, "Test title", "Test content", 0, 2)
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/post.py
    # And see what happens when you run this test again.
