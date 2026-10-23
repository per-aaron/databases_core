from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository

class Application():
    def __init__(self):
        # Connect to the database
        self.connection = DatabaseConnection()
        self.connection.connect()
        # Seed with some seed data
        self.connection.seed("seeds/student_directory_2.sql")

    def run(self):
        print("Welcome to the cohort search")
        print("\n")
        print("Which cohort would you like to list?")
        print(" Enter a number between 1 and 5 (inclusive)")
        print("\n")
        num = input("Enter your choice: ")
        print("\n")

        cohort_repository = CohortRepository(self.connection)
        print(cohort_repository.find_with_students(num))



if __name__ == '__main__':
    app = Application()
    app.run()