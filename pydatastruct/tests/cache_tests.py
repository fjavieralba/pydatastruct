import unittest
from cache.cache import BetterLRU

class BetterLRUTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_lru(self):
        lru = BetterLRU(3)
        self.assertFalse(lru.is_full())