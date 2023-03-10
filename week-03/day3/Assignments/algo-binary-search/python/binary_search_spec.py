import random
from binary_search import binary_search

test_array = [1, 2, 3, 4, 5]

print(binary_search(1, test_array) == 0)
print(binary_search(2, test_array) == 1)
print(binary_search(3, test_array) == 2)
print(binary_search(4, test_array) == 3)
print(binary_search(5, test_array) == 4)


super_big_array = [1, 5, 7, 2, 3, 8, 4, 9]
print(binary_search(7, super_big_array) == 5)
print(binary_search(6, super_big_array) == -1)


values = random.sample(list(range(1,10000)), 1000)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

print(binary_search(537, values))