from .student import Student
from .staff import Staff
# import sys
# sys.path.append('week-02/day3/Assignments/oop-school-interface-i')


class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students()
        self.staff = Staff.all_staff()
