# PYTHON OOP (OBJECT ORIENTED PROGRAMING)

# Principals of OOP:
# Encapsulation = Data access can be restricted based on needs (covered today)
# Abstraction = Logic/Complexity is hidden, for simplicity (covered today)
# Inheritance = Sharing of similar features and attributes (covered Wednesday)
# Polymorphism = Objects can take different forms depending on needs/situation (covered Wednesday)





class Dog:    #--Class Definition
  legs = 4    #-- class variable
  eyes = 2
  
  def __init__(self, name='no name provided', breed='no breed provided', color='no color provided'): #-- dunder method (double under)
    self.name = name
    self.breed = breed
    self.color = color
  
  def change_leg_count(self):   #--- effects all instances of class Dog
    Dog.legs -= 1
  
  def display_info(self):   #-- instance method
    print(f"dogs have {self.eyes} eyes and {self.legs} legs.")
    print(f"my dogs name is {self.name}, the breed is {self.breed}, color is {self.color}")

fido = Dog('fido', 'pit', 'brown')#-- create an instance of our Dog class

print(fido.display_info())




class Employee:
  number_of_employees = 0
  raise_amount = 1.04
  
  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.pay = pay
    self.email = f"{first_name}.{last_name}@email.com.lower()"
    
    Employee.number_of_employees += 1
    
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)
      
  def display_info(self):
    return f"{self.first_name, self.last_name}"
    
  def __str__(self):
    pass
      
      
employee_1 = Employee('Alice', 'Kay', 50000)
print (Employee.number_of_employees)
employee_2 = Employee('Gordo','Pat',100000)
print(Employee.number_of_employees)
print (employee_1.display_info())

class Dog:
    def __init__(self, name, breed, color, sound):
        self.name = name
        self.breed = breed
        self.color = color
        self.sound = sound

    def __str__(self):
        return f"I am a {self.color} {self.breed} dog named {self.name} and I say {self.sound}!"

    def speak(self):
        print(f">> {self.sound}")
        
    def fetch(self, item):
        print(f">> {self.name} fetched the {item}")

fido = Dog("Fido", "Pointer", "white", "woof!")
print(fido) # this is a much more descriptive output! This text comes from the __str__() instance method

lassie = Dog("Lassie", "Collie", "golden", "ruff!")
print(lassie)      

print(lassie.fetch('ball'))



import csv

animal_type = input('cats or dogs')
try:
  data = open(f'./data/{animal_type}.csv')
  reader = csv.DictReader(data)
  
  for row in reader:
    print(f"{row['name']} is a {row['age']} year old {row["breed"]}.")
  data.close()
except:
  print(f"Sorry, we don't have any {animal_type} here.")