class Bst:
  def __init__(self):
    self.parent = None

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    if not self.parent:
      self.parent = Node(value)
    else: 
      self._insert(value, self.parent)
      
  def _insert(self, value, cur_node):
    if value < cur_node.data:
      if not cur_node.left:
        cur_node.left = Node(value)
      else:
        self._insert(value, cur_node.left)
    elif value > cur_node.data:
      if not cur_node.right:
        cur_node.right = Node(value)
      else:
        self._insert(value, cur_node.right)
    else:
      print("Value already in tree")

  def contains(self, value):
    # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
    itr = self.parent
    while True:
      if not itr:
        return False
      if itr.data == value:
        return True
      elif itr.data < value:
        itr = itr.right
      elif itr.data > value:
        itr = itr.left
 

  def remove(self, value):
    # this is where you will remove a value from the BST
    if self.contains(value):
      itr = self.parent
      while True:
        if itr.right.value == value:
          if itr.right.left:
            itr.right = itr.right.left
            itr2 = itr.right
            while True:
              if itr2.right
          else:
            itr.right = itr.right.right
        elif itr.data < value:
          itr = itr.right
        elif itr.data > value:
          itr = itr.left



# ----- Node ------
class Node:
  # store your DATA and LEFT and RIGHT values here
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  



a_linked_list = Bst()
a_linked_list.insert(100)
a_linked_list.insert(50)
a_linked_list.insert(110)
a_linked_list.insert(57)
a_linked_list.insert(90)
a_linked_list.insert(120)
a_linked_list.insert(200)
a_linked_list.insert(98)
a_linked_list.insert(115)


print(a_linked_list.contains(57))
print(a_linked_list.contains(98))
print(a_linked_list.contains(101))


