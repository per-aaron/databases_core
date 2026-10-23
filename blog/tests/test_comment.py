from lib.comment import Comment

#Comment constructs with id, title and contents. comments as None
def test_comment_constructs():
    comment = Comment(1, "Commenter", "a comment", 2)
    assert comment.id == 1
    assert comment.author == "Commenter"
    assert comment.content == "a comment"
    assert comment.post_id == 2

#We can format comments to strings nicely
def test_comment_formats_nicely():
    comment = Comment(1, "Commenter", "a comment", 2)
    assert str(comment) == "Comment(1, Commenter, a comment, 2)"

#We can compare two identical comments
#and have them equal
def test_comments_are_equal():
    comment1 = Comment(1, "Commenter", "a comment", 2)
    comment2 = Comment(1, "Commenter", "a comment", 2)
    assert comment1 == comment2