from classes.staff import Staff
from classes.student import Student
class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
    def list_students(self):
        # return self.students
        lists = self.students
        count = 0
        output = ''
        for student in lists:
            count += 1
            output += f"{count}. {student.name} {student.school_id} \n"
        print(output)
    def find_student_by_id(self, student_id):
        lists = self.students
        output = ''
        for student in lists:
            if student.school_id == student_id:
                return student.__str__()