# Django ORM

## Object-Relational Mapping

-   Walk through creating a Django project with Django App
-   Changing Settings to link to PostgreSQL
-   Migrate built in Django Data Tables to Postgres with psycopg2
-   Create a student Data Table
    -   What does the Migrations Folder do?
    -   How to update Data Tables?
    -   How to drop the Data Base
-   Inserting Data into data tables
    -   Utilizing the Django Shell
    -   Utilizing fixtures
        - dumpdat 
            -   ex: python manage.py dumpdata school_app.Students
        - loaddata
            -   ex: python manage.py loaddata data.json
    -   Interacting with Data through views
-   Front-End to Back-End to ORM
    -   working with axios
    -   creating a view with csrf_exempt


## Stretch Goals to Exercise

Create the ability to click on a student and be redirected to a Student Information template where you could see all studen data.

-   Requirements
    -   Create anchor tags for students to provided path
    -   Add two fields to the Student model [Boolean, Floatfield]
    -   Create the student_info view to query the database and render the correct template.