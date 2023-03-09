from clean_data import clean_database
from build_db import build_db
import psycopg

def initiate_database_build():
    database = './employee_info.csv'
    clean_db = (clean_database(database))
    print(build_db(clean_db))


def questions(question):
    connection = psycopg.connect(f"dbname=chicago_salaries")
    results = connection.execute(question)
    print(results.fetchall())
    connection.commit()
    connection.close()
    

question1 = ("SELECT * FROM employees WHERE employees.annual_salary = (SELECT MAX(annual_salary) FROM employees);")
question2 = ("SELECT * FROM employees where employees.annual_salary = (SELECT MIN(annual_salary) FROM employees);")
question3 = ("SELECT department, AVG(annual_salary) AS avg_salary FROM employees GROUP BY department ORDER BY avg_salary DESC limit 1")
question4 = ("SELECT department, AVG(annual_salary) AS avg_salary FROM employees GROUP BY department ORDER BY avg_salary ASC limit 1")
question5 = ("SELECT SUM(avg_salary)/2 from (SELECT AVG(annual_salary) as avg_salary FROM employees GROUP BY full_or_part_time order by full_or_part_time DESC limit 2) as foo;")
question6 = ("SELECT first_name, COUNT(first_name) AS times_found FROM employees GROUP BY first_name ORDER BY times_found DESC LIMIT 1;")
question7 = ("SELECT last_name, COUNT(last_name) AS times_found FROM employees GROUP BY last_name ORDER BY times_found DESC LIMIT 1;")
question8 = ("SELECT first_name, last_name, job_title, department, annual_salary FROM employees WHERE (first_name, last_name) IN (SELECT first_name, last_name FROM employees GROUP BY first_name, last_name HAVING count(*)>1) ORDER BY first_name, last_name;")

# questions(question1)
# questions(question2)
# questions(question3)
# questions(question4)
# questions(question5)
# questions(question6)
# questions(question7)
# questions(question8)
