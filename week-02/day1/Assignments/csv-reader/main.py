import csv

class Animal:
    def __init__(self, type, name, age, breed):
        self.type = type
        self.name = name
        self.age = age
        self.breed = breed

    def about(self):
        return (f"{self.name} is a {self.breed} type of {self.type} and is {self.age} years old.")

    def update_age(self, num):
        self.age = num

    def get_age(self):
        return self.age

    def get_type(self):
        return self.type

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name


def create_animal_file(animal_type):
    want_to_add = (input(
        f"We do not have a file containing {animal_type}s, would you like to create one? Yes/No:  ")).lower()
    if want_to_add == 'yes':
        f = open(f'data/{animal_type}s.csv', 'w')
        f.write('name, age, breed\n')
        f.close()
        print(f'File called {animal_type}s.csv created, please continue:')
        return (add_adoptable())
    return (f"No new files created")


def add_adoptable():
    animal_type = (input(
        "What type of animal would you like to add?(ie: cat, dog...):  ")).lower()
    try:
        with open(f'data/{animal_type}s.csv', 'r') as my_file:
            pass
    except FileNotFoundError:
        return (create_animal_file(animal_type))
    with open(f'data/{animal_type}s.csv', 'a') as my_file:
        name = input(f"What is the {animal_type}'s name?:  ")
        breed = input(f"What breed of {animal_type} is {name}?:  ")
        age = input(f"How old is {name} in years?:  ")
        my_file.write(f"{name}, {age}, {breed} \n")
    return (f"{name} has been added to the database")


def adoptables(animal):
    try:
        animal = animal.lower()
        if animal[(len(animal))-1] != 's':
            animal = animal + 's'
        with open(f'data/{animal}.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    print(f"-->{row[0]} is a{row[1]} year old{row[2]}.")
        return ('Report done')
    except FileNotFoundError:
        return (f"Sorry, we don't have any {animal} here")


def routing():
    while True:
        header = (input(
            " To get a list of adoptable animals type: 'list' \n To add an animal type: 'add' \n To exit, type: 'exit' \n >:  ")).lower()
        if header == 'list':
            animal_type = input(f"What type?:  ")
            print(adoptables(animal_type))
        elif header == "add":
            print(add_adoptable())
        elif header == 'exit':
            return ('Have a wonderful day')
        else:
            print('That was not an option.')


print(routing())
