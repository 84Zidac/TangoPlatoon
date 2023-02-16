from .person import Person
# import sys
import csv
# sys.path.append('week-02/day3/Assignments/oop-school-interface-i')

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
      super().__init__(name, age, role, password)
      self.school_id = school_id
      
    @staticmethod  
    def all_students():
      student_obj_list = []
      with open('week-02/day3/Assignments/oop-school-interface-i/data/students.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
          student_obj_list.append(Student(**row))
      return student_obj_list
      