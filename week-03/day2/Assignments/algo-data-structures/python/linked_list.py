class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self, head = None):
        self.head = head
        self.length = 0
        
    def add(self, data):
        # write your code to ADD an element to the Linked List
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        self.length += 1

    def remove(self, data):
        if self.head == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.value != data:
                itr = itr.next
            else:
                itr.next = itr.next.next
                return
        return('Item does not exist')
                
            

    def get(self, element_to_get):
        # write you code to GET and return an element from the Linked List
        itr = self.head
        if element_to_get > self.length:
            return None
        i = 1
        while i < element_to_get:
            itr = itr.next
            i += 1
        return itr.value.value

# ----- Node ------


class Node:
    # store your DATA and NEXT values here
    def __init__(self, value):
        self.value = value
        self.next = None



a = Node(23)
b = Node(78)
c = Node(46)

a_linked_list = LinkList()
a_linked_list.add(a)
a_linked_list.add(b)
a_linked_list.add(c)
print(a_linked_list.get(2))









