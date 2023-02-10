
# modes_of_transportation = ['car', 'bicycle', 'van']

# if 'car' in modes_of_tansporatation:
#   print(true)

# my_dict = {
#     "donuts": "yummy!",
#     "green beans": "icky!",

# if donuts in foods:
#   print(true)
  
# if dounts in foods.keys():

# if 'icky!' in food.values():
#--------------------------------------------------------------------------------------

# SWITCH CASES

# lang = input("What's the programming language you want to learn? ")

# match lang:
#     case "JavaScript":
#         print("You can become a web developer.")

#     case "Python":
#         print("You can become a Data Scientist")

#     case "Java":
#         print("You can become a mobile app developer")
    
#     case "PHP":
#         print("You can become a backend developer")
    
#     case "Solidity":
#         print("You can become a Blockchain developer")    
    
#     case _:
#         print("The language doesn't matter, what matters is solving problems.")
        
#--------------------------------------------------------------------------------------
#LAMDA FUNCTIONS    
        
#      ## typical function example
# def add_one(x):
#     return x + 1

# print(add_one(7)) # output would be 8

# ## lambda function example
# add_two = lambda x : x + 2

# print(add_two(7)) # output would be 9   
        
# add = lambda num, num2 : num + num2

# print(add(8,2))     

#--------------------------------------------------------------------------------------
#LIST METHODS

# #.MAP

# my_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = list(map(lambda item : item + 2, my_list))
# # new_list = list(new_map)
# for x in new_list:
#     print(x)

# print(list(new_list)) # need to cast as a list
## [3,4,5,6,7,8,9,10,11,12]
#-------------------
####FILTER

# my_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = list(filter(lambda item : item % 3 == 0, my_list))
# # new_list=list(new_filter)
# for x in new_list:
#     print(x)

# print(new_list) # need to cast as a list
# ## [3,6,9]

#-------------------

####REDUCE

# import functools
# my_list = [1,2,3,4,5,6,7,8,9,10]
# sum = functools.reduce(lambda agg, item : agg * item, my_list)
# print(sum)

#-------------------
####SORT

# people = [
#     {
#         'name': 'alice',
#         'age': 44,
#         'job': 'influencer',
#     },
#     {
#         'name': 'bob',
#         'age': 49,
#         'job': 'dog walker',
#     },
#     {
#         'name': 'carol',
#         'age': 35,
#         'job': 'life coach',
#     },
# ]
# # This sorts the original list
# # people.sort(key=lambda k : k['age'])
# # print(people)

# # key is a 1-argument function that describes how to sort the list.
# # This returns a new list (original list is not modified)
# # people_sorted = sorted(people, key=lambda k : k['age'],reverse=True) 
# # print(people_sorted)

# new_people_list = sorted(people, key= lambda person: person['age'])

# print(new_people_list)

#-------------------
####ZIP
# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)
# print(zipped)  # Holds an iterator object
# #<zip object at 0x7fa4831153c8>
# print(type(zipped))
# #<class 'zip'>
# # print(list(zipped))
# # [(1, 'a'), (2, 'b'), (3, 'c')]
# print(dict(zipped))


#--------------------------------------------------------------------------------------
#TRY EXCEPT

# try:
#   a = 1
#   b = 2
#   c = "donuts"
  
#   d = a + b
#   print(d)

#   e = b/0 # error
#   print(e)
# except ZeroDivisionError as e:
#   print('stop dividing by zero')
# except:
#     # handle exception
#     print("BOO! there was an error")
# else:
#     # handle success
#     print("YAY! there was no error")
# finally:
#     # always execute regardless of exception or success
#     print("donuts are yummy!")

# # except Exception as e:
# #   # prints out exception
# #   print(e)

# # except ZeroDivisionError as e:
# #   print('stop dividing by zero')



#--------------------------------------------------------------------------------------
#MODULES

## file1.py
# def say_hello():
#     print('Hey there')
# def say_goodbye():
#     print('Bye bye')

## file2.py
# import file1 as anything
# from file1 import say_goodbye
# from file1 import *
# # import '../day3/challenges/algo-factorial/python/factorial'

# print(anything.say_hello())
# print(say_goodbye())
# print(factorial(4))


#--------------------------------------------------------------------------------------
#FILES READ & WRITE

import os

# print(os.getcwd())   # absolute path

# './file1.py' # relative path

# print(os.path.abspath('file1')) # it just appends the absolute path
# print(os.path.abspath('../day2/algo-factorial/python/factorial.py'))


# file = open('example.txt') # opens with read permissions only
# for line in file:
#   print(line)
# file.close() # must close after 'open'

# with open('example.txt') as file: 
#   print(file.read())# automatically closes
#   for line in file:
#     print(line)

# R is for read
# W is for write
# X is for create
# A is for append

# with open('example.txt', 'a') as file:
#   lines = ['apple\n', 'pear\n', 'carrot\n']
#   file.write('whatever\n')
#   file.writelines(lines)
  


