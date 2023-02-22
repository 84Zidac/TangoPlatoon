class Stack:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
    def __init__(self):
        self._stack = []
        self._size = 0

    def push(self, data):
        # write your code to add data following LIFO and return the Stack
        if self._stack == []:
            self._stack.append(data)
            self._size += 1
            return self._stack
        self._stack.append(self._stack[self.size()-1])
        i = self.size()
        while i > 0:
            self._stack[i] = self._stack[i-1]
            i -= 1
        self._size += 1
        self._stack[0] = data
        return self._stack

    def pop(self):
        # write your code to removes the data following LIFO and return the Stack
        if self.size() == 0:
            return None
        del self._stack[0]
        self._size -= 1
        return self._stack

    def size(self):
        # write your code that returns the size of the Stack
        return self._size


my_stack = Stack()
print(my_stack.push(5))
print(my_stack.push(4))
print(my_stack.push(3))
print(my_stack.push(2))
print(my_stack.push(1))
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
