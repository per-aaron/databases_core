from lib.cohort import Cohort
from datetime import date

#Cohort constructs with id, name and starting_date
def test_cohort_constructs():
    cohort = Cohort(1, "Test cohort", date(1980, 9, 21))
    assert cohort.id == 1
    assert cohort.name == "Test cohort"
    assert cohort.starting_date == date(1980, 9, 21)
    assert cohort.students == None

#We can format cohorts to strings nicely
def test_cohort_formats_nicely():
    cohort = Cohort(1, "Test cohort", date(1980, 9, 21))
    assert str(cohort) == "Cohort(1, Test cohort, 1980-09-21, None)"

#We can compare two identical cohorts
#and have them equal
def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Test cohort", date(1980, 9, 21))
    cohort2 = Cohort(1, "Test cohort", date(1980, 9, 21))
    assert cohort1 == cohort2