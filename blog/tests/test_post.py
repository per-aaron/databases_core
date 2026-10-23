from lib.post import Post

#Post constructs with id, title and contents. comments as None
def test_post_constructs():
    post = Post(1, "Test Post", "Here is a post")
    assert post.id == 1
    assert post.title == "Test Post"
    assert post.content == "Here is a post"
    assert post.comments == None

#We can format posts to strings nicely
def test_post_formats_nicely():
    post = Post(1, "Test Post", "Here is a post")
    assert str(post) == "Post(1, Test Post, Here is a post, Comments: None)"

#We can compare two identical posts
#and have them equal
def test_posts_are_equal():
    post1 = Post(1, "Test Post", "Here is a post")
    post2 = Post(1, "Test Post", "Here is a post")
    assert post1 == post2