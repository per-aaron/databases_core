from lib.student import Student

#student constructs with id, name and cohort_id
def test_student_constructs():
    student = Student(1, "Test student", 4)
    assert student.id == 1
    assert student.name == "Test student"
    assert student.cohort_id == 4

#We can format students to strings nicely
def test_student_formats_nicely():
    student = Student(1, "Test student", 4)
    assert str(student) == "Student(1, Test student, 4)"

#We can compare two identical students
#and have them equal
def test_students_are_equal():
    student1 = Student(1, "Test student", 4)
    student2 = Student(1, "Test student", 4)
    assert student1 == student2