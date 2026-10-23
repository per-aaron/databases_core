class Post:
    def __init__(self, id, title, content, comments = None):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, Comments: {self.comments})"

    def __eq__(self, value):
        return self.__dict__ == value.__dict__