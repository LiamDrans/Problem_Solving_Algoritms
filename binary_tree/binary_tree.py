class BinaryTree:
    def __init__(self, data=None):
        self.root = None
        if data:
            self.root = Node(data)

    def append(self, data):

            self.len += 1

            if not self.root:
                self.root = Node(data)
                return

            node = self.root

            for bit in bin(self.len)[3:-1]:
                node = [node.left, node.right][int(bit)]
            if self.len & 1:
                node.right = Node(data)
            else:
                node.left = Node(data)


class Node:
    def __init__(self, data):
        self.binary_tree_code = (0, 0)
        self.left = None
        self.right = None
        self.data = data
