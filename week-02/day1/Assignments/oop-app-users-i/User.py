# your User class goes here


class User:
    def __init__(self, first_name, last_name, email, drivers_licence='not provided', age='not provided', sex='not provided', location='not provided'):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__drivers_licence = drivers_licence
        self.__age = int(age)
        self.__sex = sex
        self.__location = location

    def __str__(self):
        return f"Name={self.__last_name, self.__first_name} \n Email: {self.__email} \n Drivers Licence ={self.__drivers_licence} \n Age={self.__age} Sex={self.__sex} \n Location= {self.__location}"


dave = User('Dave', 'Jones', 'dj@email.com', 'SAE123', '34', 'M', 'Texas')
tom = User('Tom', 'Smith', 'Toms@email.com', 'ABC890', '20', 'M', 'Utah')
sue = User('Sue', 'Best', 'best_sue@email.com', 'JWE653', '55', 'F', 'Kansas')

print(dave)
