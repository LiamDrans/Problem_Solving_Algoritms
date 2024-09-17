class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add(self, data):

        if self.length == 0:
            self.head = Node(data)
            self.tail = self.head
        
        elif self.length == 1:
            self.head.next = Node(data)
            self.tail = self.head.next
        
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.length += 1

    def delete(self, data):
        if isinstance(data, Node) and data == self.head or data == self.head.data:
                self.head = self.head.next
                self.length -= 1
                print(f"Head node '{[data.data if isinstance(data, Node) else data][0]}' deleted")
                return True
        if self.head.next:
            curr_node = self.head.next
            prev_node = self.head
            while curr_node:
                if isinstance(data, Node) and data == curr_node or data == curr_node.data:
                    if curr_node.next:
                        prev_node.next = curr_node.next
                        curr_node.next = None
                        print(f"Inner node '{[data.data if isinstance(data, Node) else data][0]}' deleted")
                        self.length -= 1
                    else:
                        prev_node.next = None
                        print(f"Tail node '{[data.data if isinstance(data, Node) else data][0]}' deleted")
                        self.length -= 1
                prev_node = curr_node
                curr_node = curr_node.next

    def listing(self):
        return_list = []
        curr_node = self.head
        while curr_node:
            return_list.append(curr_node.data)
            curr_node = curr_node.next
        return return_list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


