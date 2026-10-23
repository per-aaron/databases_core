from lib.comment import Comment
from lib.post import Post

class PostRepository:
    def __init__(self, conn):
        self.connection = conn

    def find_with_comments(self, post_id):
        rows = self.connection.execute(
            "SELECT posts.id as post_id, posts.title, posts.content as post_content, comments.id as comment_id, comments.author, comments.content as comment_content " \
            "FROM posts JOIN comments ON posts.id = comments.post_id " \
            "WHERE posts.id = %s", [post_id]
        )
        if rows == []:
            return "No comments found! Try find() instead!"
        comments = []
        for row in rows:
            comment = Comment(row["comment_id"], row["author"], row["comment_content"], row["post_id"])
            comments.append(comment)
        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)