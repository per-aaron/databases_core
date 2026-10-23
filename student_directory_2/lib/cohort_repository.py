from lib.student import Student
from lib.cohort import Cohort

class CohortRepository:
    def __init__(self, conn):
        self.connection = conn

    def find_with_students(self, cohort_id):
        rows = self.connection.execute(
            "SELECT cohorts.id as cohort_id, cohorts.name as cohort_name, cohorts.starting_date, students.id as student_id, students.name, students.cohort_id " \
            "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
            "WHERE cohorts.id = %s", [cohort_id]
        )
        students = []
        for row in rows:
            student = Student(row["student_id"], row["name"], row["cohort_id"])
            students.append(student)

        return Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], rows[0]["starting_date"], students)