class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.total = 0
    self.inqueue = []

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.inqueue.append(data)
    self.total += 1
    return self.inqueue

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
        if self.size() == 0:
            return None
        value = self.inqueue[0]
        del self.inqueue[0]
        self.total -= 1
        return value

  def size(self):
    # write your code that returns the size of the Queue
    return self.total

my_queue = Queue()
print(my_queue.enqueue(5))
print(my_queue.enqueue(4))
print(my_queue.enqueue(3))
print(my_queue.enqueue(2))
print(my_queue.enqueue(1))
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())









