from .person import Person
# import sys
import csv
# sys.path.append('week-02/day3/Assignments/oop-school-interface-i')

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
      super().__init__(name, age, role, password)
      self.employee_id = employee_id
      
      
    @staticmethod  
    def all_staff():
      staff_obj_list = []
      with open('week-02/day3/Assignments/oop-school-interface-i/data/staff.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
          staff_obj_list.append(Staff(**row))
      return staff_obj_list