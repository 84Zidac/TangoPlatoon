import psycopg
import csv

## Let's connect to our database
connection = psycopg.connect(f"dbname=class_roster")

## Let's create a query to create a students table and execute it
connection.execute("DROP TABLE IF EXISTS students")
student_table_creation_query = "CREATE TABLE students (id serial PRIMARY KEY, first_name varchar,last_name varchar, email varchar, favorite_food varchar);"
connection.execute(student_table_creation_query)
# hardcoded values are not very useful
# connection.execute("INSERT INTO students (name, favorite_food) VALUES ('Alice', 'Cake')")


# danger! danger!
# name="Bob"
# food="Lemons"
# connection.execute(f"INSERT INTO students (name, favorite_food) VALUES ('{name}', '{food}')")

# SQL injection attack
# name="Malory', 'apples'); DROP TABLE students;--"
# food="Pizza"
# connection.execute(f"INSERT INTO students (name, favorite_food) VALUES ('{name}', '{food}')")

# query params help avoid SQL injection, but they can become hard to read if we have many of them, or if any of them are repeated
first_name="Carol"
last_name='King'
food="Tuna"
connection.execute("INSERT INTO students (name, favorite_food) VALUES (%s, %s)", (name, food))

name="Dan"
food="Bagels"
connection.execute("INSERT INTO students (name, favorite_food) VALUES (%(name)s, %(food)s)", {'name':name, 'food':food})

results = connection.execute("SELECT * FROM students;")
print(results.fetchall())

with open('./students.csv', mode='r', skipinitialspace = True) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=', ')
    for student in students_reader:
        create_student_statement = create_insert_student_query

connection.commit()
connection.close()