import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def test_init_with_no_args(self):
        """ creates an empty list by default """
        l = LinkedList()
        self.assertTrue(l.isEmpty())
    
    def test_not_empty(self):
        """ isEmpty returns false for not empty list """
        l = LinkedList([1,2,3])
        self.assertFalse(l.isEmpty())
    
    def test_empty_list_size_0(self):
        self.assertEqual(LinkedList().size(), 0)

    def test_append_one_element_not_empty(self):
        """ append adds elements to the list """
        l = LinkedList()
        l.append(1)
        self.assertFalse(l.isEmpty())
    
    def test_append_one_element_size(self):
        """ append adds elements to the list """
        l = LinkedList()
        l.append(1)
        self.assertEqual(l.size(), 1)

    def test_append_multiple_elements(self):
        l = LinkedList()
        l.append(1)
        l.append(7)
        self.assertTrue(l.size() == 2)
    
    def test_prepend_one_elemen(self):
        l = LinkedList([4,5,6])
        l.prepend(1)
        self.assertTrue(l.getElementAtIndex(0) == 1)
    
    def test_prepend_multiple_elements(self):
        l = LinkedList([2, 3, 4])
        l.prepend(1)
        l.prepend(0)
        self.assertTrue(l.getElementAtIndex(0) == 0)
        self.assertTrue(l.getElementAtIndex(1) == 1)
    
    def test_get_first_element_empty_list(self):
        l = LinkedList()
        with self.assertRaises(RuntimeError):
            l.getElementAtIndex(0)
    
    def test_delete_first_occurence(self):
        l = LinkedList([1,2,2,3])
        l.deleteFirstOccurence(2)
        self.assertEqual(l.to_python_list(), [1, 2, 3])
    
    def test_delete_first_occurence_empty_list(self):
        l = LinkedList()
        original_python_list = l.to_python_list()
        l.deleteFirstOccurence(7)
        modified_python_list = l.to_python_list()
        self.assertEqual(original_python_list, modified_python_list)
    
    def test_delete_at_index(self):
        l = LinkedList([1,2,3])
        l.deleteAtIndex(1)
        self.assertEqual(l.to_python_list(), [1, 3])
    
    def test_delete_at_index_emtpy_list(self):
        l = LinkedList()
        with self.assertRaises(RuntimeError):
            l.deleteAtIndex(0)
    
    def test_delete_at_index_out_of_bound(self):
        l = LinkedList([1,2,3])
        with self.assertRaises(RuntimeError):
            l.deleteAtIndex(7)
    

