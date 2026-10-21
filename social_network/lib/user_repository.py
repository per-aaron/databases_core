from lib.user import User

class UserRepository:
    def __init__(self, conn):
        self.connection = conn

    def all(self):
        rows = self.connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = User(row["id"], row["username"], row["email"])
            users.append(user)

        return users

    def find(self, user_id):
        rows = self.connection.execute(
            "SELECT * FROM users WHERE id = %s", [user_id])
        row = rows[0]
        return User(row['id'], row['username'], row['email'])

    def create(self, user):
        self.connection.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s)",
            [user.username, user.email])
        return None

    def delete(self, user_id):
        self.connection.execute(
            "DELETE FROM users WHERE id = %s", [user_id]
        )
        return None