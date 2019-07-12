import unittest
from double_linked_list import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_with_no_args(self):
        """ creates an empty list by default """
        l = DoubleLinkedList()
        self.assertTrue(l.isEmpty())