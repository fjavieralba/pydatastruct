class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, python_list = None):
        """ creates a new empty list """
        self.head = Node(None)
        if python_list is not None:
            for elem in python_list:
                self.append(elem)

    def isEmpty(self):
        return self.head.next == None
    
    def size(self):
        size = 0
        current_node = self.head
        while not current_node.next is None:
            current_node = current_node.next
            size += 1
        return size

    def append(self, data):
        current_node = self.head
        while not current_node.next is None:
            current_node = current_node.next
        current_node.next = Node(data)
    
    def prepend(self, data):
        new_node = Node(data)
        previous_first = self.head.next
        self.head.next = new_node
        new_node.next = previous_first

    def deleteFirstOccurence(self, data):
        if self.isEmpty():
            return
        current_node = self.head.next
        if current_node.data == data:
            self.head.next = current_node.next
            return
        next_node = current_node.next
        while next_node is not None and next_node.data != data:
            current_node = next_node
            next_node = next_node.next
        if next_node.data == data:
            current_node.next = next_node.next
    
    def deleteAtIndex(self, index):
        if self.isEmpty():
            raise RuntimeError("cannot delete in empty list")
        current_node = self.head.next
        if index == 0: #remove first element
            self.head.next = current_node.next
            return
        next_node = current_node.next
        current_position = 0
        while next_node is not None and current_position + 1< index:
            current_node = next_node
            next_node = next_node.next
            current_position += 1
        if current_position + 1 == index:
            current_node.next = next_node.next
        else:
            raise RuntimeError("out of bounds") 
    
    def getElementAtIndex(self, index):
        if self.isEmpty():
            raise RuntimeError("empty list")
        current_node = self.head.next
        current_position = 0
        while current_node.next is not None and current_position < index:
            current_node = current_node.next
            current_position +=1
        if current_position == index:
            return current_node.data
        else:
            raise RuntimeError("out of bounds")
    
    def to_python_list(self):
        if self.isEmpty():
            return []
        python_list = []
        current_node = self.head.next
        while current_node.next is not None:
            python_list.append(current_node.data)
            current_node = current_node.next
        python_list.append(current_node.data)
        return python_list
