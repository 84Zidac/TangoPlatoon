# a_small_number = 4
# print(type(a_small_number)) ------> int

#------------------------------------------------------

# a_string = 'hello world'
# another_string = "welcome to the internet"
# print(type(another_string))

# day = 'Friday'
# activity = 'bowling'
# print(f"Let's go {activity} on {day} afternoon.") # This is sometimes called an "f string"

# name = 'someone\'s name'
# print(name) ----> "someone's name"

# ------------------------------------------------------------------------------------------------------
#LISTS

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
#TUPLES

# days_of_the_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
# days_of_the_week[6] = 'Caturday' # this throws an error! we can't assign to a tuple

#-------------------------------------------------------------------------------------------------------
#DICTIONARY

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

#--------------------------------------------------------------------------
#FUNCTIONS

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
def who_am_i(**kwargs):
    for kwarg in kwargs: # we'll talk more about loops in a minute
        print(f'My {kwarg} is {kwargs[kwarg]}.')
#who_am_i(name='dan', age=20, job='skydiving instructor')#---------> my name is dan, my age is 20, my job is skydiving instructor
jeff = {
    'name': 'jeff',
    'age': 44,
    'job': 'influencer',
}
#print(jeff['age'])


print(who_am_i(**jeff))



# ------------------------------------------------------------------------------------------------------------------------------------------










