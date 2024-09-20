class BinaryTree:
    def __init__(self, data=None):
        self.root = None
        if data:
            self.root = Node(data)

class Node:
    def __init__(self, data):
        self.binary_tree_code = (0, 0)
        self.left = None
        self.right = None
        self.data = data
