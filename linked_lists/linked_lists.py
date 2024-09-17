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
            self.length += 1
        
        elif self.length == 1:
            self.head.next = Node(data)
            self.tail = self.head.next
            self.length += 1
        
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.length += 1

    def listing(self):
        return_list = []
        for i in range(self.length):
            if i == 0:
                return_list.append(self.head.data)
            else:
                next_str = "next."
                eval_str = f"self.head.{next_str*i}data"
                return_list.append(eval(eval_str)) # works but need to refactor to a iterator
        return return_list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


