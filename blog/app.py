from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

class Application():
    def __init__(self):
        # Connect to the database
        self.connection = DatabaseConnection()
        self.connection.connect()
        # Seed with some seed data
        self.connection.seed("seeds/blog.sql")

    def run(self):
        print("Welcome to the blog search")
        print("\n")
        print("Which blog post would you like to list?")
        print(" Enter a number between 1 and 4 (inclusive)")
        print("\n")
        num = input("Enter your choice: ")
        print("\n")

        post_repository = PostRepository(self.connection)
        print(post_repository.find_with_comments(num))



if __name__ == '__main__':
    app = Application()
    app.run()