import unittest
from double_linked_list import DoubleLinkedList, Node

class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_with_no_args(self):
        """ creates an empty list by default """
        l = DoubleLinkedList()
        self.assertTrue(l.is_empty())
    
    def test_append_single_elem(self):
        l = DoubleLinkedList()
        n = Node('data')
        l.append(n)
        self.assertFalse(l.is_empty())
        self.assertEqual(l.head, n)
    
    def test_append_then_prepend(self):
        l = DoubleLinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.append(n1)
        l.prepend(n2)
        self.assertEqual(l.head, n2)
    
    def test_get_on_empty_list(self):
        l = DoubleLinkedList()
        with self.assertRaises(RuntimeError):
            l.get_at_index(5)
    
    def test_get_at_index(self):
        l = DoubleLinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l.append(n1)
        l.prepend(n2)
        l.append(n3)
        self.assertEqual(l.get_at_index(0), n2)
        self.assertEqual(l.get_at_index(1), n1)
        self.assertEqual(l.get_at_index(2), n3)
    
    def test_get_at_index_out_of_bounds(self):
        l = DoubleLinkedList()
        l.append(Node(1))
        with self.assertRaises(RuntimeError):
            l.get_at_index(5)
