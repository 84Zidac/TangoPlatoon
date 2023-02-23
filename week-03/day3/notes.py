# # Simple Factoral

# def factorial(n):
#     result = 1

#     for i in range(n, 1, -1):
#         result *= i

#     return result


# print(factorial(1))       # 1
# print(factorial(5))       # 120
# print(factorial(100))     # 9.332621544394418e+157

# #-------------------------------------------------------------------------------
# # Recursive factoral

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)


# print(factorial(1))       # 1
# print(factorial(5))       # 120
# print(factorial(100))     # 9.332621544394418e+157


# #-------------------------------------------------------------------------------
# # Stack Overflow

# def factorial(n):
#     return n * factorial(n-1)


# print(factorial(5))  # RecursionError: maximum recursion depth exceeded


# #-------------------------------------------------------------------------------
# # Binary Search Tree
# # Notice the substructure
# class BinaryTree:
#     def __init__(self, value, left, right):
#         self.value = value
#         self.left = left
#         self.right = right

# # a Binary Search Tree (BST) is any Tree with the property that
# # every node's left value is smaller than the node's own value
# # every node's right value is greater than the node's own value


# myTree = BinaryTree(
#     56,
#     BinaryTree(
#         22,
#         BinaryTree(
#             10,
#             None,
#             None
#         ),
#         BinaryTree(
#             30,
#             None,
#             BinaryTree(
#                 44,
#                 None,
#                 None
#             )
#         )
#     ),
#     BinaryTree(
#         81,
#         BinaryTree(
#             77,
#             None,
#             None
#         ),
#         BinaryTree(
#             92,
#             None,
#             None
#         )
#     ),
# )

# # Represented as a tree:
# #
# #                     56
# #                  /      \
# #                22        81
# #              /   \     /    \
# #            10    30   77    92
# #                    \
# #                    44

# #-------------------------------------------------------------------------------
# # Binary Search 

# class BinaryTree:
#     def __init__(self, value, left, right):
#         self.value = value
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return f"[{self.value}, {self.left}, {self.right}]"


# myTree = BinaryTree(56,
#                     BinaryTree(22,
#                                BinaryTree(10, None, None),
#                                BinaryTree(30,
#                                           None,
#                                           BinaryTree(44, None, None))),
#                     BinaryTree(81,
#                                BinaryTree(77, None, None),
#                                BinaryTree(92, None, None)))

# # Represented as a tree:
# #
# #                     56
# #                  /      \
# #                22        81
# #              /   \     /    \
# #            10    30   77    92
# #                    \
# #                    44

# # looks for a value in the tree, assuming BST structure. returns the subtree if found, otherwise None if cit's not in the tree.


# def binarySearch(tree, value):
#     # if we call BinarySearch on an empty tree (which we will do in recursive cases) return None
#     if tree == None:
#         return None

#     if value == tree.value:
#         return tree
#     elif value < tree.value:
#         return binarySearch(tree.left, value)
#     else:
#         return binarySearch(tree.right, value)


# print(binarySearch(myTree, 1))



#-------------------------------------------------------------------------------
# Recursion

# Factorial (imperative)
# 4! = '!' just means factoral so, 4*3*2*1






