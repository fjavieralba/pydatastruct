import unittest
from cache.cache import BetterLRU

class BetterLRUTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_lru(self):
        lru = BetterLRU(3)
        self.assertFalse(lru.is_full())
    
    def test_lru_put(self):
        lru = BetterLRU(3)
        lru.put('a', 1)
        lru.put('b', 2)
        lru.put('c', 3)
        self.assertTrue(lru.is_full())
        self.assertEqual(lru.get('a'), ('a', 1))
    
    def test_lru_put_more(self):
        lru = BetterLRU(3)
        lru.put('a', 1)
        lru.put('b', 2)
        lru.put('c', 3)
        lru.put('d', 4)
        with self.assertRaises(RuntimeError):
            lru.get('a')
        lru.get('b')
        lru.put('e', 5)
        with self.assertRaises(RuntimeError):
            lru.get('c')

        
        
