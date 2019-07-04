### Binary Search Tree ###

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data):
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
    
    def contains(self, data):
        if data == self.data:
            return True
        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.contains(data)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(data)
    
    def print_in_order(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

    def __repr__(self):
        return "({}) <{}> ({})".format(self.left, self.data, self.right)