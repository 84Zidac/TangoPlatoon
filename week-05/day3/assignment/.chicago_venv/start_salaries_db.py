import psycopg

connection = psycopg.connect(f"dbname=chicago_salaries")

connection.execute("DROP TABLE IF EXISTS employees")
student_table_creation_query = "CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar,last_name varchar, job_title varchar, full_or_part_time varchar, department varchar, annual_salary);"











