from lib.cohort import Cohort
from lib.cohort_repository import CohortRepository
from lib.student import Student
from datetime import date

#Find a cohort along with all its students
def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, "Leander", date(1930,9,8), [
        Student(1, 'Jervis', 1),
        Student (2, 'Jackal', 1),
        Student(3, 'Juno', 1)
    ])