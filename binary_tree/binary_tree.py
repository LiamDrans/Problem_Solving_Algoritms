class BinaryTree:
    def __init__(self, data=None, name="BinaryTree"):
        self.root = None
        self.len = 0
        self.name = name
        if data:
            self.len = 1
            self.root = Node(data)

    def _return_parent_by_data(self, data):

        node = self.root

        for i in reversed(range(self.len+1)[1:]):
            for bit in bin(i)[3:-1]:
                node = [node.left, node.right][int(bit)]
            print(node.data)
            if i & 1:
                if node.right.data == data:
                    return (node, int(bin(i)[-1]))
            else:
                if node.left.data == data:
                    return (node, int(bin(i)[-1]))
            node = self.root

    def _return_parent_by_position(self, position):

        node = self.root
        for bit in bin(position)[3:-1]:
            node = [node.left, node.right][int(bit)]
        return (node, int(bin(position)[-1]))

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
                return (node.data, i)
            else:
                node = self.root
        print(f"{data} not found in {self.name}.")
        return False
    
    def delete(self, data):

        del_position = self.find(data)[1]
        print(del_position)

        parent_node = self._return_parent_by_data(data)
        final_parent_node = self._return_parent_by_position(self.len)
        replacing_node = [final_parent_node[0].right if final_parent_node[1] & 1 else final_parent_node[0].left][0]

        if self.root.data == data:
            right = self.root.right
            left = self.root.left
            self.root = replacing_node
            self.root.right = right
            self.root.left = left
        else:
            if parent_node[1] & 1:
                if final_parent_node[1] & 1:
                    replacing_node.right = parent_node[0].right.right
                    replacing_node.left = parent_node[0].right.left
                    parent_node[0].right = replacing_node
                    final_parent_node[0].right = None
                else:
                    replacing_node.right = parent_node[0].right.right
                    replacing_node.left = parent_node[0].right.left
                    parent_node[0].right = replacing_node
                    final_parent_node[0].left = None
            else:
                if final_parent_node[1] & 1:
                    replacing_node.right = parent_node[0].left.right
                    replacing_node.left = parent_node[0].left.left
                    parent_node[0].left = replacing_node
                    final_parent_node[0].right = None
                else:
                    replacing_node.right = parent_node[0].left.right
                    replacing_node.left = parent_node[0].left.left
                    parent_node[0].left = replacing_node
                    final_parent_node[0].left = None

        self.len -= 1

        if del_position == self.len+1:
            print(f"{data} successfully deleted from the end of {self.name}.")
        else:
            print(f"{data} successfully deleted, {replacing_node.data} replaced at {self.name} position {del_position}.")
        

class Node:
    def __init__(self, data):
        self.binary_tree_code = (0, 0)
        self.left = None
        self.right = None
        self.data = data
