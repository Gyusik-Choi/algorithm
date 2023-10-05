from unittest import TestCase


class Node:
    def __init__(self, char, word=None):
        self.char = char
        self.word = word
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for idx, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = Node(char)

            cur = cur.children[char]

        cur.word = word

    def exist(self, word):
        cur = self.head

        for idx, char in enumerate(word):
            if char not in cur.children:
                return False

            cur = cur.children[char]

        if cur.word:
            return True

        return False

    def start_with_prefix(self, prefix):
        cur = self.head
        answer = []

        for idx, p in enumerate(prefix):
            if p not in cur.children:
                return []

            cur = cur.children[p]

        # prefix 도 trie 에 포함되어 있다면 answer 에 넣어준다
        if cur.word:
            answer.append(cur.word)

        return self.find_words(cur, answer)

    def find_words(self, node, words):
        for key, value in node.children.items():
            if value.word:
                words.append(value.word)

            if value.children:
                self.find_words(value, words)

        return words


class TrieTest(TestCase):
    def test_start_with_prefix(self):
        t = Trie()
        t.insert('A')
        t.insert('ABC')
        t.insert('ABCD')
        t.insert('BCD')
        t.insert('ACD')
        t.insert('ADG')
        t.insert('ABD')
        result = t.start_with_prefix('A')
        self.assertEqual(result, ['A', 'ABC', 'ABCD', 'ABD', 'ACD', 'ADG'])
