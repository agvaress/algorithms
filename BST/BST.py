'''
        10
       /  \
      5   15
     / \  / \
    2  5 13 22
   /      \
  1       14
'''

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


root = Node(10)
root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(5)
root.left.left.left = Node(1)

root.right.left = Node(13)
root.right.left.right = Node(14)
root.right.right = Node(22)
