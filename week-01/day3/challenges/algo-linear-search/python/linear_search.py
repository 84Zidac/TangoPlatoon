array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)


def linear_search(value_to_find, array_to_search_through):
    for i, value in enumerate(array_to_search_through):
        print(i, value)
        if value == value_to_find:
            return i


def linear_search_global(value_to_find, array_to_search_through):
    list = []
    for i, value in enumerate(array_to_search_through):
        print(i, value)
        if value == value_to_find:
            print(i, value)
            list.append(i)
            print(list)
    return list

def compareArrays (array1, array2):

    if len(array1) != len(array2):
        return False
   
    for element in array1:
        
        if element not in array2:
            return False
  
    return True


print(linear_search(3, [1,2,3]) == 2)
print(linear_search(4, [1,2,3]) == None)
print(linear_search(13, [1,2,3]) == None)
# print(compareArrays(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]), [1, 3, 5]))
print(compareArrays(linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]), [6]))
# print(compareArrays(linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]), [2, 4]))
