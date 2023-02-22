
# # this function does not make widgets. it makes functions that create widgets
# def widgetMakerMaker(widget_color):

# 	# this function actually makes widgets
# 	def widgetMaker():
# 		return {
# 			'type': 'widget',
# 			'color': widget_color,
# 		}

# 	# return the function we just created, so it can be used outside of WidgetMakerMaker
# 	return widgetMaker

# redWidgetMaker = widgetMakerMaker('red')
# red_widget = redWidgetMaker()
# another_red_widget = redWidgetMaker()

# blueWidgetMaker = widgetMakerMaker('blue')
# blue_widget = blueWidgetMaker()
# another_blue_widget = blueWidgetMaker()

# --------------------------------------------------------------------------------------
# Decorators -- functions that allow us to modify the behavior of another function


# from datetime import datetime

# def AddOne(num):
# 	return num + 1

# def MultiplyByTwo(num):
# 	return num * 2

# # This function accepts a function as input, then returns a new function that behaves similarly to the one that is passed in
# def PrintCurrentTimeAndAlso(func):

# 	# this function accepts any number of positional arguments (*args) and any number of named arguments (**kwargs)
# 	def WrapperFunction(*args, **kwargs): # can take in any arugments sent into it
# 		print(f'Calling {func.__name__} at {datetime.now()}')
# 		return func(*args, **kwargs)

# 	return WrapperFunction

# # This creates a new, decorated function
# PrintCurrentTimeAndAlsoAddOne = PrintCurrentTimeAndAlso(AddOne)   #this is a function to print the time and add 1
# one_plus_one = PrintCurrentTimeAndAlsoAddOne(1) # This is just using the above function to add 1 to 1 and will print current time.


# # This creates a new, decorated function
# PrintCurrentTimeAndAlsoMultiplyByTwo = PrintCurrentTimeAndAlso(MultiplyByTwo)
# two_times_two = PrintCurrentTimeAndAlsoMultiplyByTwo(2)

# # Using the decorator syntax (@) allows us to create a decorated function all at once,
# # instead of creating an undecorated function, and then passing it into the decorator
# @PrintCurrentTimeAndAlso  # this replaces line 46
# def SubtractThree(num):
# 	return num - 3

# nine_minus_three = SubtractThree(9)

# ------------------------------------------------------------------------------------------------------------------------------
# Instance Attributes vs Class Atributes
# class Dog:
# 	species = "Canis Lupus Familiaris" # all dogs have the same species type => *class attribute*
# 	legs = 4

# 	def __init__(self, name, breed, color, sound):
# 		self.name = name # each dog has a unique name => *instance attribute*
# 		self.breed = breed
# 		self.color = color
# 		self.sound = sound

#   def speak(self):
#     print(self.sound)

# fido = Dog("Fido", "Pointer", "white", "woof!")
# print(fido.name)
# print(fido.species)

# lassie = Dog("Scooby", "Mutt", 'brown', "Scooby-Dooby-Doo!")
# print(lassie.speak())
# print(lassie.name)
# print(lassie.species)

# ------------------------------------------------------------------------------------------------------------------------------
# Instance Methods -vs- Class Methods -vs- Static Methods


# import math

# class Pizza:
#     def __init__(self, radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients

#     def area(self):
#         return self.circle_area(self.radius)

#     @staticmethod # this makes it able to be called by dot notation ie line 98, can be access inside and outside the class
#     def circle_area(r):
#         return r ** 2 * math.pi

#     @classmethod # same as static but sends out all properties of class
#     def margherita(cls, rad):
#         return cls(rad, ['mozzarella', 'tomatoes'])

#     @classmethod
#     def prosciutto(cls, rad):
#         return cls(rad, ['mozzarella', 'tomatoes', 'ham'])


# my_pizza = Pizza(8, ['mushrooms', 'pineapple'])
# print(my_pizza.area())

# my_pizza2 = Pizza.margherita(9)

# print(my_pizza2.ingredients)

# ------------------------------------------------------------------------------------------------------------------------------
# Getters and Setters


# class Person:
#     def __init__(self):
#         self._age = 0
#         self.dead = False

#     # using property decorator
#     # a getter function
#     @property # makes it an instance attribute or makes it a property of Person
#     def age(self):
#         print("getter method called")
#         return self._age

#     # a setter function
#     @age.setter # points at the above function 'age' and says that it is its setter.
#     def age(self, a):
#         self._age = a
#         print('calling getter method')
#         if (a > 100):
#             self.dead = True


# alice = Person()

# alice.newage = 19
# print(alice.newage)
# # print(alice._age)
