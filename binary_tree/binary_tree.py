class BinaryTree:
    def __init__(self, data=None, name="BinaryTree"):
        self.root = None
        self.len = 0
        self.name = name
        if data:
            self.len = 1
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

    def find(self, data):

        node = self.root

        for i in reversed(range(self.len+1)[1:]):
            for bit in bin(i)[3:]:
                node = [node.left, node.right][int(bit)]
            if node.data == data:
                print(f"{data} found at position {i} of {self.name}.")
                return (node.data, i)
            else:
                node = self.root
        print(f"{data} not found in {self.name}.")
        return False



class Node:
    def __init__(self, data):
        self.binary_tree_code = (0, 0)
        self.left = None
        self.right = None
        self.data = data
