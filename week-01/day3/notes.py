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



# Main function to holding 2 dictionaries, the string to be returned, and routes information to helper functions.
# def optimal_change(cost, paid_with):
#     if cost > paid_with:
#         return ("Need more money.")
#     if cost == paid_with:
#         return ("Exact change")
#     # finds the amount of change needing to be returned
#     change = paid_with - cost
#     converted = round(change * 100)     # converts the change to a whole number
#     change_dict = {                     # Dictionary holding how many of each denomination of money needs returned
#         'hundred_bill': 0,
#         'fifty_bill': 0,
#         'twenty_bill': 0,
#         'ten_bill': 0,
#         'five_bill': 0,
#         'one_bill': 0,
#         'quarter': 0,
#         'dime': 0,
#         'nickel': 0,
#         'penny': 0
#     }
#     conversion_dict = {  # Dictionary used to refrerence how much each denomination is worth in cents
#         'hundred_bill': 10000,
#         'fifty_bill': 5000,
#         'twenty_bill': 2000,
#         'ten_bill': 1000,
#         'five_bill': 500,
#         'one_bill': 100,
#         'quarter': 25,
#         'dime': 10,
#         'nickel': 5,
#         'penny': 1
#     }
#     built_str = (
#         f'The optimal change for an item that costs ${cost} with an amount paid of ${paid_with} is')  # This is where the entire string to be returned is built
#     for denom in conversion_dict:  # loops through conversion_dict
#         # starting with the highest denomination, if it is needed to make change, find how many and add that to the change_dict while subtracting that amount from converted
#         if conversion_dict[denom] <= converted:
#             number_of_denom = converted // conversion_dict[denom]
#             change_dict[denom] = int(number_of_denom)
#             converted -= number_of_denom * conversion_dict[denom]

#     for denom in change_dict:  # for each denomination that needs returned and is greater than 0, sends the denomination, number of the denomination, and value of the denomination into the 'string maker' function and concantinates it to built_str
#         if change_dict[denom] > 0:
#             add_str = string_maker(
#                 denom, change_dict[denom], conversion_dict[denom])
#             built_str = built_str + str(add_str)

#     # sends built_str into finalize_str function in order to find the last comma to make it a period and add an 'and' after the 2nd to last comma.
#     final_str = finalize_str(built_str)
#     return final_str


# def string_maker(denom, num_of_denom, value):
#     # handles all of the bills and sees whether it should add an 'S' to bill.
#     if value > 99:
#         if num_of_denom > 1:
#             return (f' {num_of_denom} ${int(value/100)} bills,')
#         else:
#             return (f' {num_of_denom} ${int(value/100)} bill,')
#     elif denom != 'penny':  # handles the coin change except for pennies deciding if the denomination requires an 'S' or not
#         if num_of_denom > 1:
#             return (f' {num_of_denom} {denom}s,')
#         else:
#             return (f' {num_of_denom} {denom},')
#     else:
#         if num_of_denom > 1:  # handles pennies because it is more complicated than just adding an 's' to penny
#             return (f' {num_of_denom} pennies,')
#         else:
#             return (f' {num_of_denom} penny,')


# def finalize_str(str):
#     indx = str.rfind(',')       # finds the index of the last comma
#     final_list = list(str)  # changes the string 'final_list' into a string
#     final_list[indx] = '.'      # replaces the comma with a period
#     str = ''.join(final_list)   # turns it back into a string
#     # reassigns indx in order to identify the 2nd to last comma
#     indx = str.rfind(',')
#     if indx != -1:            # if a 2nd comma is found, it does the same as above but replaces it with ', and'
#         final_list = list(str)
#         final_list[indx] = ', and'
#         return ''.join(final_list)
#     return ''.join(final_list)    # returns the final string






# print(optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

# Main function to holding 2 dictionaries, the string to be returned, and routes information to helper functions.
# def optimal_change(cost, paid_with):
# #   try:
#     if cost > paid_with:
#         return ("Need more money.")
#     if cost == paid_with:
#         return ("Exact change")
#     # finds the amount of change needing to be returned
#     change = paid_with - cost
#     converted = round(change * 100)     # converts the change to a whole number
#     change_dict = {                     # Dictionary holding how many of each denomination of money needs returned
#         'hundred_bill': {'name': 'hundred_bill','count': 0, 'value': 10000},
#         'fifty_bill': {'name': 'fifty_bill','count': 0, 'value': 5000},
#         'twenty_bill': {'name': 'twenty_bill','count': 0, 'value': 2000},
#         'ten_bill': {'name': 'ten_bill','count': 0, 'value': 1000},
#         'five_bill': {'name': 'five_bill','count': 0, 'value': 500},
#         'one_bill': {'name': 'one_bill','count': 0, 'value': 100},
#         'quarter': {'name': 'quarter','count': 0, 'value': 25},
#         'dime': {'name': 'dime','count': 0, 'value': 10},
#         'nickel': {'name': 'nickel','count': 0, 'value': 5},
#         'penny': {'name': 'penny','count': 0, 'value': 1},
#     }
#     # for key, value in change_dict.items():
#     #   print(value['value'])
 
#     built_str = (
#         f'The optimal change for an item that costs ${cost} with an amount paid of ${paid_with} is')  # This is where the entire string to be returned is built
#     for key, value in change_dict.items(): 
#         print(value)# loops through conversion_dict
#         # starting with the highest denomination, if it is needed to make change, find how many and add that to the change_dict while subtracting that amount from converted
#         if value['value'] <= converted:
#             number_of_denom = converted // value['value']
#             change_dict[key]['count'] = int(number_of_denom)
#             converted -= number_of_denom * value['value']
#             # print(change_dict)

#     for key, value in change_dict.items():  # for each denomination that needs returned and is greater than 0, sends the denomination, number of the denomination, and value of the denomination into the 'string maker' function and concantinates it to built_str
#         if value['count'] > 0:
#             add_str = string_maker(value)
#             built_str = built_str + str(add_str)

#     # sends built_str into finalize_str function in order to find the last comma to make it a period and add an 'and' after the 2nd to last comma.
#     final_str = finalize_str(built_str)
#     print(final_str)
#     return final_str
# #   except:
# #     print('Input needs to be either an intiger or a float')


# def string_maker(denom):
#     if denom['value'] > 99:
#         if denom['count'] > 1:
#             return (f" {denom['count']} ${int(denom['value']/100)} bills,")
#         else:
#             return (f" {denom['count']} ${int(denom['value']/100)} bill,")
#     elif denom['name'] != 'penny':  # handles the coin change except for pennies deciding if the denomination requires an 'S' or not
#         if denom['count'] > 1:
#             return (f" {denom['count']} {denom['name']}s,")
#         else:
#             return (f" {denom['count']} {denom['name']},")
#     else:
#         if denom['count'] > 1:  # handles pennies because it is more complicated than just adding an 's' to penny
#             return (f" {denom['count']} pennies,")
#         else:
#             return (f" {denom['count']} penny,")


# def finalize_str(str):
#     indx = str.rfind(',')       # finds the index of the last comma
#     final_list = list(str)  # changes the string 'final_list' into a string
#     final_list[indx] = '.'      # replaces the comma with a period
#     str = ''.join(final_list)   # turns it back into a string
#     # reassigns indx in order to identify the 2nd to last comma
#     indx = str.rfind(',')
#     if indx != -1:            # if a 2nd comma is found, it does the same as above but replaces it with ', and'
#         final_list = list(str)
#         final_list[indx] = ', and'
#         return ''.join(final_list)
#     return ''.join(final_list) 






# print(optimal_change('test', 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
    # indx = str.rfind(',')       # finds the index of the last comma
    # final_list = list(str)  # changes the string 'final_list' into a string
    # final_list[indx] = '.'      # replaces the comma with a period
    # str = ''.join(final_list)   # turns it back into a string
    # # reassigns indx in order to identify the 2nd to last comma
    # indx = str.rfind(',')
    # if indx != -1:            # if a 2nd comma is found, it does the same as above but replaces it with ', and'
    #     final_list = list(str)
    #     final_list[indx] = ', and'
    #     return ''.join(final_list)
    # return ''.join(final_list)    # returns the final string



# Write your solution here!
# Sudo Sudo:
# Create dictinary with denominations in order to track how many of each piece of money will need returned
# find how many bills/coins will be needed for each
# if it is divisable by 100, put how many times in a variable and so on for each piece of money
# dynamically build string to return the answer


def optimal_change(item_cost, amount_paid):
    '''TAKES IN THE COST OF AN ITEM AND THE AMOUNT PAID, AND RETURNS A STRING OF OPTIMAL CHANGE'''
    try:
        if item_cost > amount_paid:
            return "Need more money."
        if item_cost == amount_paid:
            return "Exact change, nothing to be returned"
        # finds the amount of change needing to be returned
        change = amount_paid - item_cost
        # converts the change to a whole number
        converted = round(change * 100)
        change_dict = {                     # Dictionary holding name of each denomination, how many needs returned, and the value of each denomination.
            'hundred_bill': {'name': 'hundred_bill', 'count': 0, 'value': 10000},
            'fifty_bill': {'name': 'fifty_bill', 'count': 0, 'value': 5000},
            'twenty_bill': {'name': 'twenty_bill', 'count': 0, 'value': 2000},
            'ten_bill': {'name': 'ten_bill', 'count': 0, 'value': 1000},
            'five_bill': {'name': 'five_bill', 'count': 0, 'value': 500},
            'one_bill': {'name': 'one_bill', 'count': 0, 'value': 100},
            'quarter': {'name': 'quarter', 'count': 0, 'value': 25},
            'dime': {'name': 'dime', 'count': 0, 'value': 10},
            'nickel': {'name': 'nickel', 'count': 0, 'value': 5},
            'penny': {'name': 'penny', 'count': 0, 'value': 1},
        }

        built_str = (
            f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is')  # This is where the entire string to be returned is built
        for key, value in change_dict.items():  # loops through conversion_dict returning the key of each nexted dictionary and the values of each
            # starting with the highest denomination, if the denomination is needed to make change, find how many and add that to the change_dict while subtracting that amount from converted
            if value['value'] <= converted:
                number_of_denom = converted // value['value']
                value['count'] = int(number_of_denom)
                converted -= number_of_denom * value['value']

        for key, value in change_dict.items():  # for each denomination that needs returned and is greater than 0, sends the denomination, number of the denomination, and value of the denomination into the 'string maker' function and concantinates it to built_str
            if value['count'] > 0:
                add_str = string_maker(value)
                built_str = built_str + str(add_str)

        # sends built_str into finalize_str function in order to find the last comma to make it a period and add an 'and' after the 2nd to last comma.
        final_str = finalize_str(built_str)
        return final_str
    except TypeError:
        return 'Error: Please input the cost of the item as the first argument and amount paid in the second argument. Both need to be either an intiger or a float'


def string_maker(denom_dict):
    '''TAKES IN A DICTIONARY OF THE DENOMINATION AND OUTPUTS THE CHANGE IN TEXT.'''
    if denom_dict['value'] > 99:  # handles dollar and above
        if denom_dict['count'] > 1:
            return f" {denom_dict['count']} ${int(denom_dict['value']/100)} bills,"
        return f" {denom_dict['count']} ${int(denom_dict['value']/100)} bill,"
    # handles the coin change except for pennies deciding if the denomination requires an 'S' or not
    if denom_dict['name'] != 'penny':
        if denom_dict['count'] > 1:
            return f" {denom_dict['count']} {denom_dict['name']}s,"
        return f" {denom_dict['count']} {denom_dict['name']},"
        # handles pennies because it is more complicated than just adding an 's' to penny
    if denom_dict['count'] > 1:
        return f" {denom_dict['count']} pennies,"
    return f" {denom_dict['count']} penny,"


def finalize_str(fix_str):
    '''TAKES IN THE FINAL STRING AND REPLACES THE LAST 2 COMMAS WITH AN 'AND' AND A PERIOD '''
    indx = fix_str.rfind(',')       # finds the index of the last comma
    final_list = list(fix_str)  # changes the string 'final_list' into a string
    final_list[indx] = '.'      # replaces the comma with a period
    fix_str = ''.join(final_list)   # turns it back into a string
    # reassigns indx in order to identify the 2nd to last comma
    indx = fix_str.rfind(',')
    if indx != -1:            # if a 2nd comma is found, it does the same as above but replaces it with ', and'
        final_list = list(fix_str)
        final_list[indx] = ', and'
    return ''.join(final_list)
