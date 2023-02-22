# # Data structures: data orzanization, management, and storage format
# #arrays(list), objects (dictionaries)

# data = ['a', 'x', 'y', 'g', 'n','b']

# data.append('L') # adds 'L' to the end of the array - O(1)

# data.insert(0, 'q') # adds 'q' to the start of the array - O(n) since it has to shift all elements over

# location_of_g = data.index('g') # searching for a value in an array - O(n)


# # a sorted array of letters
# data = ['a', 'c', 'l', 'm', 'r', 't', 'x']
# data.addButKeepSorted('n') #  O(n)

# # searching a sorted list is O(log n), because we can use binary search


class HashTable :
    def __init__(self) :
        
        self.table = [[] for i in range(64)]   # creates a list of 64 lists


    # given a key, this function should return a numerical index, which we can use to access the table above
    def _hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)  # returns an integer representing a unicode character

        return hash % len(self.table)


    def set(self, key, value):
        index = self._hash(key)
        self.table[index].append([key,value])
    

    def get(self, key):
        index = self._hash(key)

        for data in self.table[index]:
            if data[0] == key  :
                return data[1]
            


myHash = HashTable()

myHash.set('name', 'alice')
myHash.set('age', 34)
myHash.set('mane', 'luxurious') # this key will cause a hash collision with 'name', because they are anagrams

print(myHash.table)
print(myHash.get('name'))
print(myHash.get('age'))
print(myHash.get('mane'))

