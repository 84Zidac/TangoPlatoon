import csv

        
def clean_data(csv_row):
    [last_name, first_name] = csv_row['Name'].split(',')
    first_name = first_name.strip()
    last_name = last_name.strip()
    try:
        [first_name, mid] = first_name.split(' ')
    except ValueError:
        mid = 'NMN'
    cleaned = {}
    cleaned['first_name'] = first_name
    cleaned['last_name'] = last_name
    cleaned['job_title'] = csv_row['Job Titles']
    cleaned['department'] = csv_row['Department']
    cleaned['full_or_part_time'] = csv_row['Full or Part-Time']
    try:
        cleaned['annual_salary'] = float(csv_row['Annual Salary'])
    except ValueError:
        cleaned['annual_salary'] = float(csv_row['Hourly Rate']) * int(csv_row['Typical Hours']) * 50

    return cleaned

def clean_database(db_link):
    cleaned_lst = []
    with open(db_link, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for employee in csv_reader:
            clean_row = clean_data(employee)
            cleaned_lst.append(clean_row)
    return cleaned_lst
        