class LinkedList:
    def __init__(self, name="Linked List"):
        self.head = None
        self.tail = None
        self.length = 0
        self.name = name
        self.psn = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __next__(self):
        eval_str = f"self.head{'.next'*self.psn}"
        self.psn += 1
        return next(LinkedListIterator(eval(eval_str))) #to be refactored
  
    def __len__(self):
        return self.length

    
    def append(self, data):

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

    def find(self, data, curr_node = None, position=0):
        if not curr_node:
            curr_node = self.head
        if isinstance(data, Node) and data == curr_node or data == curr_node.data:
            print(f"Node '{[data.data if isinstance(data, Node) else data][0]}' found at position {position} of {self.name}")
            return (True, position)
        elif curr_node.next:
            return self.find(data, curr_node.next, position+1)
        else:
            if isinstance(data, Node) and data == curr_node or data == curr_node.data:
                print(f"Node '{[data.data if isinstance(data, Node) else data][0]}' found at position {position} of {self.name}")
                return (True, position)
            print(f"Node '{[data.data if isinstance(data, Node) else data][0]}' not found in {self.name}")
            return (False, None)

    def reverse(self):
        prev_node = None
        curr_node = self.head
        old_head = self.head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        self.tail = old_head
        self.tail.next = None

class LinkedListIterator:
    def __init__(self, head):
        self.curr_node = head

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.curr_node:
            raise StopIteration
        else:
            value = self.curr_node
            self.curr_node = self.curr_node.next
            return value.data

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


