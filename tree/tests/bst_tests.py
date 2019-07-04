import unittest
from bst import Node

class TestBST(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_insert_element(self):
        t = Node(10)
        t.insert(7)
        self.assertTrue(t.contains(7))
    
    def test_add_several_elements(self):
        t = Node(7)
        t.insert(14)
        t.insert(21)
        t.insert(3)
        self.assertTrue(t.contains(3))