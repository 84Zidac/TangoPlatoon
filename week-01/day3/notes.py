# a_small_number = 4
# print(type(a_small_number)) ------> int

# ------------------------------------------------------

# a_string = 'hello world'
# another_string = "welcome to the internet"
# print(type(another_string))

# day = 'Friday'
# activity = 'bowling'
# print(f"Let's go {activity} on {day} afternoon.") # This is sometimes called an "f string"

# name = 'someone\'s name'
# print(name) ----> "someone's name"

# ------------------------------------------------------------------------------------------------------
# LISTS

# berries = ['grape', 'tomato', 'cucumber', 'eggplant', 'banana', 'watermelon', 'pumpkin']
# berries.append('carrots')----> makes another list inside berries
# print(type(berries)) # list
# print(berries[1]) # normal indexing works how you'd expect
# print(berries[-1]) # index from the back of the list
# print(berries[2:4]) # slice in the middle
# print(berries[:3]) # slice from the start to index 3
# print(berries[2:]) # slice from index 2 to the end
# barries.remove('tomato')
# barries.insert(2,'someberry') ---------> insert into index 2

# ----------------------------------------------------------------------------------------------------
# TUPLES

# days_of_the_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
# days_of_the_week[6] = 'Caturday' # this throws an error! we can't assign to a tuple

# -------------------------------------------------------------------------------------------------------
# DICTIONARY

# jeff = {
#     'name': 'jeff',
#     'age': 44,
#     'job': 'influencer',
# }
# print(jeff['age'])

# people = [
#     {
#         'name': 'alice',
#         'age': 44,
#         'job': 'influencer',
#     },
#     {
#         'name': 'bob',
#         'age': 31,
#         'job': 'dog walker',
#     },
#     {
#         'name': 'carol',
#         'age': 65,
#         'job': 'life coach',
#     },
# ]
# print(people[1]['name'])

# --------------------------------------------------------------------------
# FUNCTIONS

# def gimme_five():
#     return 5
# print(gimme_five() + 10)


# # if a function is defined with one parameter, it must be called with one argument
# def add_one(n):
#     return n + 1
# print(add_one(10))

# # order matters for positional arguments
# def describe_berries(n=1, color='blue'):
#     print(f'I have {n} {color}berries.')
# describe_berries(3, 'blue')
# describe_berries(color='black', n=4)

# # keyword arguments can be used in any order
# def describe_berries(n=1, color="blue"):
#     print(f'I have {n} {color}berries.')
# describe_berries(color="rasp", n=3)

# # use * to define a function with an unspecified number of parameters
# def print_them_all(*args):
#     print(args)
# print_them_all('alice', 'bob', 'carol')


# use ** to define a function with an unspecified number of keyword arguments
# def who_am_i(**kwargs):
#     for kwarg in kwargs: # we'll talk more about loops in a minute
#         print(f'My {kwarg} is {kwargs[kwarg]}.')
# who_am_i(name='dan', age=20, job='skydiving instructor')#---------> my name is dan, my age is 20, my job is skydiving instructor
# jeff = {
#     'name': 'jeff',
#     'age': 44,
#     'job': 'influencer',
# }
# print(jeff['age'])


# print(who_am_i(**jeff))


# ------------------------------------------------------------------------------------------------------------------------------------------

# SETS
# my_list=[1, 24, 5, 7, 43, 4, 5, 1]
# s={1,2,3}
# s=set(my_list)
# print(s)
# print(list(s))

# -----------------------------------------------------------------
# IF STATEMENTS
# def can_drink_beer(age, country):
#     if age >= 21 or age >= 18 and country == 'Canada':
#         return True
#     elif country == 'Antarctica':
#         return True
#     else:
#         return False

# print(can_drink_beer(20, 'USA'))
# print(can_drink_beer(21, 'USA'))
# print(can_drink_beer(18, 'Canada'))


# ----------------------------------------------------------
# FOR LOOPS

# looping over list elements
# my_list = ["a", "b", "c"]
# for x in my_list:
#     print(x)

# ## loop over a range
# for x in range(10):
#     print(x)

# for x in range(4, 10):
#   print(x)

# for x in range(4, 10, 2):
#   print(x)

# for x in range(20, 0, -1):
#   print(x)

# for i, x in enumerate(my_list):
#     print(i, x)

# ## looping over dictionary entries
# my_dict = {
#     "donuts": "yummy!",
#     "green beans": "icky!",
# }
# for k in my_dict:
#     print(my_dict[k])

# for v in my_dict.values():
#     print(v) # same output as the previous loop

# for key, value in my_dict.items():
#   print(key, value)

# for char in 'some text':
#   print(char)


# -------------------------------------------------------------------------------------------
# # WHILE LOOPS
# x = 9
# while x > 0:
#   print(x)
#   x = x - 1

# # infinite loop
# x = 9
# while x > 0:
#   print("la la la")

# ----------------------------------------------------------------------------------
# BUILT IN METHODS
# first_name = 'jonathan'
# print(first_name.capitalize()) # this is a string method that converts the first character to upper case
# print(first_name) # we see that despite running the method above, my original data does not change

# last_name = 'Young'
# print(last_name.replace('g', '123'))
# print(last_name) # same case here - this is a non destructive method

# staff = ['jon', 'rod', 'ankur', 'chad', 'alicia']
# staff.append('tom')
# print(staff) # this is a destructive method because it alters the original
# ## Let's fire tom. He sucks.
# staff.pop()
# print(staff) # my original has been changed yet again!
# print(len(staff))
# print(len(first_name))
# print(first_name.upper())
# print(last_name.lower())
# print(last_name, end='-')
# #input(">")
# new line = \n
