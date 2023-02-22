from classes.school import School

school = School('Ridgemont High')

# for staff in school.staff:
#     print(staff.name)
# for student in school.students:
#     print(student.name)
PROMPT = """
What would you like to do?
Optoins:
    1. List All Sutdents
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
"""

while True:
    try:
        mode = int(input(PROMPT))
    except ValueError:
        print('invalid input please input number')
        continue

    if mode == 1:
        school.list_students()
    elif mode == 2:
        student_id = input('Enter student id:')
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode == 3:
        new_student = {}
        new_student['name'] = input('Name')
        new_student['age'] = input('age')
        new_student['school_id'] = input('School_id')
        new_student['password'] = input('password')
        password = input('password')
        role = 'Student'
        school.add_student(new_student)
    elif mode == 4:
        id = int(input("please enter student id"))
        updated_student_list = school.remove_student_by_id(id)
        for student in updated_student_list:
            print(str(student))
    elif mode == 5:
        break
