class Node():
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None    