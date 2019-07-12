import unittest
from hashmap.hashmap import HashMap

class HashMapTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_hashmap(self):
        h = HashMap()
        with self.assertRaises(RuntimeError):
            h.get('key')
    
    def test_add_one_element(self):
        h = HashMap()
        h.add('myKey', 123)
        self.assertEqual(h.get('myKey'), 123)
    
    def test_add_one_element_numeric_key(self):
        h = HashMap()
        h.add(123, 'myValue')
        self.assertEqual(h.get(123), 'myValue')
    
    def test_add_many_key_values_with_collisions(self):
        h = HashMap()
        for i in range(0, 1000):
            h.add(i, i)
        self.assertEqual(h.get(77), 77)
        self.assertEqual(h.get(999), 999)
