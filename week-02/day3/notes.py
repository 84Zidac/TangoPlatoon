# # before classes
# def eat(catName, food):
#     print(f"{catName} eats a {food}.")


# def meow():
#     print("meow meow!")


# cat1 = {"name": 'Whiskers', "eat": eat, "meow": meow}
# cat2 = {"name": 'Katy Purry', "eat": eat, "meow": meow}

# print(cat1["name"])
# cat1["meow"]()
# cat1["eat"](cat1["name"], "mouse")

# # after classes


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(f"{self.name} eats a {food}.")

#     def meow(self):
#         print("meow meow!")


# cat3 = Cat("Garfield")

# print(cat3.name)
# cat3.meow()
# cat3.eat("mouse")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(f"{self.name} eats a {food}.")

#     def meow(self):
#         print("meow meow!")


# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(f"{self.name} eats a {food}.")

#     def bark(self):
#         print("BARK BARK!")


# garfield = Cat('Garfield')
# garfield.eat('tuna')
# garfield.meow()

# spot = Dog('Spot')
# spot.eat('steak')
# spot.bark()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(f"{self.name} eats a {food}.")

#     def speak(self):
#         print("I'm an animal!")

# class Dog(Animal):
#     # bark() is unique to Dog, it doesn't appear on a generic Animal
#     def bark(self):
#         print("bark bark!")

#     # speak() was defined on Animal but here we (explicitly) override what was inhertited
#     def speak(self):
#         self.bark()


# class Cat(Animal):
#     def meow(self):
#         print("meow meow!")

#     def speak(self):
#         self.meow()


# # note we didn't define __init__() on Cat or Dog, they were (implicitly) inherited
# lucky = Cat('lucky')
# fido = Dog('fido')
# # they both (implciitly) inherit eat as well
# lucky.eat('mouse')
# fido.eat('chicken nugget')
# # they both inherit speak, but it's effect is different for each subclass because it was (explicitly) overridden
# lucky.speak()
# fido.speak()
# # they have their own methods (naturally)
# lucky.meow()
# fido.bark()

# # but not those of their 'siblings' (naturally)
# try:
#     lucky.bark()
# except Exception as error:
#     print(f"{type(error).__name__}: {error}")

# try:
#     fido.meow()
# except Exception as error:
#     print(f"{type(error).__name__}: {error}")




#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#    super()
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(f"{self.name} eats a {food}.")

#     def speak(self):
#         print("I'm an animal!")


# class Dog(Animal):
#     def __init__(self, name, is_service_animal):
#         # use the logic from the parent Animal class without duplicating code
#         super().__init__(name)  --------> brings in all init items from parent
#         # add some Dog-specific __init__() logic
#         self.is_service_animal = is_service_animal

#     def speak(self):
#         # notice how both 'is_service_animal' (Dog instance variable) and 'name' (Animal instance variable) are directly accessible through self
#         if self.is_service_animal:
#             print(f"{self.name} at your service")
#         else:
#             print("BARK BARK!")


# fido = Dog('Fido', False)
# sparky = Dog('Sparky', True)

# fido.speak()
# sparky.speak()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#    Internal Representation'

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         print(f"{self.name} eats a {food}.")

#     def speak(self):
#         print("I'm an animal!")


# class Dog():
#     def __init__(self, name, is_service_animal):
#         self.internal_repr_animal = Animal(name)
#         self.is_service_animal = is_service_animal

#     def speak(self):
#         if self.is_service_animal:
#             print(f"{self.internal_repr_animal.name} at your service")
#         else:
#             print("BARK BARK!")


# fido = Dog('Fido', False)
# sparky = Dog('Sparky', True)

# fido.speak()
# sparky.speak()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Multiple Inheritance

# import math


# class Person:
#     def __init__(self, name, job):
#         self.name = name
#         self.job = job

#     def work(self):
#         print(f"{self.name} is working hard as a {self.job}.")


# ben = Person("Ben", "teacher")
# ben.work()

# # just to break up the output a little
# print()


# class Computer:
#     def __init__(self, number_of_cores):
#         self.number_of_cores = number_of_cores

#     def compute(self):
#         pi = round(math.pi, self.number_of_cores)
#         print(f"Computing pi to {self.number_of_cores} decimal places: {pi}")


# toaster = Computer(1)
# toaster.compute()

# chappy = Computer(4)
# chappy.compute()

# print()


# class Cyborg(Person, Computer):
#     # note the meaning of 'super()' is ambiguous when inheriting from multiple parents
#     # so this is how you reference the specific (internal) parent object instead
#     def __init__(self, name, job, number_of_cores):
#         Person.__init__(self, name, job)
#         Computer.__init__(self, number_of_cores)

#     def work(self):
#         print(f"{self.name} has the strength of {self.number_of_cores} men! Watch:")
#         for n in range(self.number_of_cores):
#             Person.work(self)
#         print("And he is still a fully functioning computer!")
#         Computer.compute(self)


# terminator = Cyborg('Arnold', 'terminator', 8)
# terminator.work()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Why Most Languages Don't Support Multiple Inheritance (dont use this)

# class Mother:
#     def __init__(self):
#         self.first_name = "Sandra"
#         self.last_name = "Wilensky"


# class Father:
#     def __init__(self):
#         self.first_name = "Harris"
#         self.last_name = "Cohen"


# class Child(Mother, Father):------------------------------------------------------
#     def __init__(self):
#         # try swapping the order of these initalization statements
#         Father.__init__(self)
#         Mother.__init__(self)

#         self.first_name = "Benjamin"

#     def print_full_name(self):
#         print(f"{self.first_name} {self.last_name}")


# ben = Child()
# ben.print_full_name()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Why Most Languages Don't Support Multiple Inheritance (Use this one)
# class Mother:
#     def __init__(self):
#         self.first_name = "Sandra"
#         self.last_name = "Wilensky"


# class Father:
#     def __init__(self):
#         self.first_name = "Harris"
#         self.last_name = "Cohen"


# class Child():
#     def __init__(self):
#         self.first_name = "Benjamin"
#         self.father = Father()
#         self.mother = Mother()

#     def print_full_name(self):
#         print(f"{self.first_name} {self.father.last_name}")


# ben = Child()
# ben.print_full_name()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#   When to Use Inheritance

# class Client():
#     def __init__(self):
#         # a single client could have multiple Gardens, held in an array
#         self.gardens = []
#         self.payment_info = ...

# class Garden():
#     def __init__(self, garden_items):
#         #  representation of where this garden is located
#         self.address = ...
#         # an array holding GardenItems within the garden
#         self.garden_items = garden_items

# # a generic superclass that all GardenItems have in common
# class GardenItem():
#     ...

# class Grass(GardenItem):
#     ...

# class Schrub(GardenItem):
#     ...

# # a generic superclass that all Trees have in common
# class Tree(GardenItem):
#     ...

# class Maple(Tree):
#     ...

# class Oak(Tree):
#     ...

# benjamin = Client(...)
# # maybe the GardenItem initilaizer takes an id representing the type of that GardenItem
# benjamins_garden = Garden(Grass(1), Schrub(4), Schrub(12), Maple(), Oak())
# benjamin.append_garden(benjamins_garden)





