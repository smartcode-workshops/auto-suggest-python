import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = ["cat", "car", "cart", "dog", "dot"]
        for word in self.words:
            self.trie.insert(word)

    def test_insert(self):
        self.assertTrue(self.trie.insert("apple"))
        self.assertFalse(self.trie.insert("cat"))

if __name__ == '__main__':
    unittest.main()