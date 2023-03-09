import psycopg

def build_db(lst_obj):
    connection = psycopg.connect(f"dbname=chicago_salaries")
    connection.execute("DROP TABLE IF EXISTS employees")
    employee_table_creation_query = "CREATE TABLE employees (id serial PRIMARY KEY, first_name varchar,last_name varchar, job_title varchar, full_or_part_time varchar, department varchar, annual_salary numeric);"
    connection.execute(employee_table_creation_query)
    for worker_dict in lst_obj:
        connection.execute("INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s, %s)", (worker_dict['first_name'], worker_dict['last_name'], worker_dict['job_title'], worker_dict['full_or_part_time'], worker_dict['department'], worker_dict['annual_salary']))
    connection.commit()
    connection.close()
    return('Complete')
    
def insert_worker(worker_dict):
    worker_sql_str = ("INSERT INTO employees (first_name, last_name, job_title, full_or_part_time, department, annual_salary) VALUES (%s, %s, %s, %s, %s, %s)", (worker_dict['first_name'], worker_dict['last_name'], worker_dict['job_title'], worker_dict['full_or_part_time'], worker_dict['department'],worker_dict['annual_salary']))
    return str(worker_sql_str)
    