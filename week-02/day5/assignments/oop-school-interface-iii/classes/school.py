from classes.staff import Staff
from classes.student import Student


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. Name: {student.name} // Student_ID: {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
    def add_student(self, new_student):
        self.students.append(Student(**dict(new_student)))
        
    def remove_student_by_id(self, id):
        for student in self.students:3
            if id == student.id:
                self.students.remove(student)
                return self.students
