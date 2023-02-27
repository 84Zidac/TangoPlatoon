# class LinkedList():
#     def __init__(self):
#         self.head = None
        
#     def append(self, value):
#         if self.head == None:
#             self.head = LL_Node(value)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = LL_Node(value)
#     def __str__(self):
#         current = self.head
#         while current:
#             print(current.value, end=' --> ')
#             current = current.next
#         return('')

# class LL_Node():
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
        
# my_linked_list = LinkedList()
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.append(6)
# print(my_linked_list)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         l1_as_num = llToNum(l1)
#         l2_as_num = llToNum(l2)
#         total = l1_as_num + l2_as_num

#         return numToLL(total)

# def llToNum(ll):
#     sum = 0
#     factor = 1

#     current = ll
#     while current:
#         sum += current.val * factor
#         factor *= 10
#         current = current.next

#     return sum

# def numToLL(num):
#     num_as_ll = ListNode()
#     current = num_as_ll

#     while num != 0:
#         current.val = num % 10
#         num = num // 10
#         if num != 0:
#             current.next = ListNode()
#             current = current.next


#     return num_as_ll


# # ----- Node ------
# class Node:
#   # store your data Value and LEFT and RIGHT values here
#   def __init__(self, val) -> None:
#      self.value = val
#      self.right = None
#      self.left = None

# ----- BST ------

# def insert(root, value):
#     new_node = Node(value)
# # this is where you will insert a value into the Binary Search Tree
#     if root == None:
#         root = new_node
#         return root
#     else:
#         if value > root.value:
#             root.right = insert(root.right, value)
#         elif value < root.value:
#             root.left = insert(root.left, value)
#     return root
            

# def remove(root, value):
# # this is where you will remove a value from the BST
#     pass

# def search(root, value):
# # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
#     pass

#   Bredth First Search
# level by level, add top, right, left to queue, the visit all in queue and add those left and right to queue
# ----- Depth First Traversal ------
# def print_inorder(root):  # visit parent, theb left subtree then right
#   if root:
#       print_inorder(root.left)
#       print(root.value)
#       print_inorder(root.right)

# def print_preorder(root): # visit left, then parent, then right
#     if root:
#         print(root.value)
#         print_preorder(root.left)
#         print_preorder(root.right)

# def print_postorder(root): # visit left, then right then parent
#     if root:
#       print_inorder(root.left)
#       print_inorder(root.right)
#       print(root.value)


# root = None
# root = insert(root, 50)
# root = insert(root, 30)
# root = insert(root, 20)
# root = insert(root, 40)
# root = insert(root, 70)
# root = insert(root, 60)
# root = insert(root, 80)


# # print_inorder(root)
# # print_preorder(root)
# print_postorder(root)

# def coordinates(ra,dec):
    



# print(coordinates(05 35m 17.3s, −05° 23′ 28″))

print(5//2)