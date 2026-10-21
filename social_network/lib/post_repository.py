from lib.post import Post

class PostRepository:
    def __init__(self, conn):
        self.connection = conn

    def all(self):
        rows = self.connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
            posts.append(post)
        return posts

    def find(self, post_id):
        rows = self.connection.execute(
            "SELECT * FROM posts WHERE id = %s", [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])

    def create(self, post):
        self.connection.execute(
            "INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)",
            [post.title, post.content, post.views, post.user_id])
        return None

    def delete(self, post_id):
        self.connection.execute("DELETE FROM posts WHERE id = %s",
                                [post_id])
        return None