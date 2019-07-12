class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
class DoubleLinkedList:
    def __init__(self, head=None, last=None):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None
    
    def append(self, node):
        """ appends a node at the end of the list """
        if self.is_empty():
            self.head = node
            self.last = node
            node.next = None
            node.prev = None
        else:
            self.last.prev = node
            node.next = self.last
            self.last = node
    
    def prepend(self, node):
        """ adds a node to the beginning of the list """
        if self.is_empty():
            self.head = node
            self.last = node
            node.next = None
            node.prev = None
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node
    
    def get_at_index(self, index):
        if self.is_empty():
            raise RuntimeError("Empty list")
        current_index = 0
        current_node = self.head
        while current_node is not self.last:
            if index == current_index:
                return current_node
            else:
                current_index += 1
                current_node = current_node.prev
        if current_index == index:
            return current_node
        else:
            raise RuntimeError("Out of Bounds")