class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def add(self, data):
        if not self._head:
            self._head = Node(data)
        

class Node:
    def __init__(self, element):
        self.element = element
        self._next = None


