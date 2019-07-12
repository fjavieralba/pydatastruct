import unittest
from tree.trie import Node

class TestTrie(unittest.TestCase):
    
    def test_contains_empty_trie(self):
        trie = Node('*')
        self.assertFalse(trie.contains('hello'))
    
    def test_add_word(self):
        trie = Node('*')
        trie.add('hello')
        self.assertTrue(trie.contains('hello'))
        self.assertFalse(trie.contains('hell')) # not considered a word since not explicitly added
    
    def test_add_several_words(self):
        trie = Node('*')
        trie.add('hello')
        trie.add('hell')
        self.assertTrue(trie.contains('hello'))
        self.assertTrue(trie.contains('hell'))
    
    def test_word_count_under_empty_trie(self):
        trie = Node('*')
        self.assertEqual(trie.words_under('h'), 0)
        
    
    def test_word_count_under(self):
        trie = Node('*')
        trie.add('hello')
        trie.add('hell')
        trie.add('hey')
        self.assertEqual(trie.words_under('hell'), 2)
        self.assertEqual(trie.words_under('he'), 3)