class Comment:
    def __init__(self, id, author, content, post_id):
        self.id = id
        self.author = author
        self.content = content
        self.post_id = post_id

    def __eq__(self, value):
        return self.__dict__ == value.__dict__

    def __repr__(self):
        return f"Comment({self.id}, {self.author}, {self.content}, {self.post_id})"
    