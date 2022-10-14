import unittest


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = dict()


class Trie:
    def __init__(self):
        # 처음에 빈 key 로 생성을 해서
        # 트리의 맨 상단에 빈 값으로 시작할 수 있도록 한다
        # 이후 추가할 때 Node 의 인자로 단어 접두사 넣어서 생성
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for idx, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]

        # 단어의 끝을 나타냄
        # 단어의 끝에만 data 에 값이 있다
        # 그리고
        # 단어의 끝에서 해당 글자를 알 수 있음
        cur.data = word

    def search(self, word):
        cur = self.head

        for idx, char in enumerate(word):
            if char not in cur.children:
                return False

            cur = cur.children[char]

        if cur.data:
            return True

        return False

    def starts_with_prefix(self, prefix):
        cur = self.head

        for idx, char in enumerate(prefix):
            if char in cur.children:
                cur = cur.children[char]
            else:
                return []

        words = self.find_words(cur, [])
        return words

    def find_words(self, cur, words):
        for word_key, word_value in cur.children.items():
            if word_value.data:
                words.append(word_value.data)
            else:
                self.find_words(word_value, words)

        return words


class TrieVer4Test(unittest.TestCase):
    def test_insert(self):
        t = Trie()
        t.insert('ABC')
        t.insert('BCD')
        self.assertEqual(len(t.head.children), 2)

    def test_insert2(self):
        t = Trie()
        t.insert('ABC')
        t.insert('ACD')
        self.assertEqual(len(t.head.children), 1)

    def test_search_insert(self):
        t = Trie()
        t.insert('ABC')
        result = t.search('ABC')
        self.assertTrue(result)

    def test_search_insert2(self):
        t = Trie()
        t.insert('ABC')
        result = t.search('ABD')
        self.assertFalse(result)

    def test_starts_with_prefix(self):
        t = Trie()
        t.insert('ABC')
        t.insert('BCD')
        t.insert('ACD')
        t.insert('ADG')
        t.insert('ABD')
        result = t.starts_with_prefix('A')
        self.assertEqual(result, ['ABC', 'ABD', 'ACD', 'ADG'])

    def test_starts_with_prefix2(self):
        t = Trie()
        t.insert('ABC')
        t.insert('BCD')
        t.insert('ACD')
        t.insert('ADG')
        t.insert('ABD')
        result = t.starts_with_prefix('AB')
        self.assertEqual(result, ['ABC', 'ABD'])

    def test_starts_with_prefix3(self):
        t = Trie()
        t.insert('ABC')
        t.insert('BCD')
        t.insert('ACD')
        t.insert('ADG')
        t.insert('ABD')
        result = t.starts_with_prefix('C')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
