from unittest import TestCase


class Node:
    def __init__(self, char=None):
        self.char = char
        self.words = []
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur = self.head

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
                cur.children[w].words.append(word)
            cur = cur.children[w]
        cur.words.append(word)

    def search(self, word: str) -> bool:
        cur = self.head

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        if word in cur.words:
            return True
        return False

    def starts_with(self, prefix: str) -> bool:
        cur = self.head

        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]

        if cur.words:
            return True
        return False


class TrieTest(TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_search(self):
        self.trie.insert("apple")
        self.assertEqual(self.trie.search("apple"), True)
