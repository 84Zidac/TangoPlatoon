import math

def binary_search(num_to_find, array):
    
    array.sort()
    first = 0
    middle = math.trunc(len(array)/2)
    last = len(array)-1
    while True:
        if array[middle] == num_to_find:
            return middle
        if first == middle or last == middle:
            return -1
        if array[middle] > num_to_find:
            last = middle-1
            if middle == math.trunc((last-first)/2):
                middle -=1
            else:
                middle = math.trunc((last-first)/2)
        if array[middle] < num_to_find:
            first = middle
            if middle == math.trunc((last + first) / 2):
                middle += 1
            else:
                middle = math.trunc((last + first) / 2)
