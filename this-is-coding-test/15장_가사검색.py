import unittest


class Node:
    def __init__(self, char, data=None):
        self.char = char
        self.length = []
        self.data = data
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for idx, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur.children[char].length.append(len(word))
            cur = cur.children[char]

        cur.data = word

    def starts_with_prefix(self, prefix):
        cur = self.head

        for idx, char in enumerate(prefix):
            if char != "?":
                if char not in cur.children:
                    return 0

                cur = cur.children[char]
                continue

            return cur.length.count(len(prefix))


def solution(words, queries):
    answer = []
    words_length = []

    trie = Trie()
    reverse_trie = Trie()
    for idx, word in enumerate(words):
        trie.insert(word)
        reverse_trie.insert(word[::-1])
        words_length.append(len(word))

    for idx, query in enumerate(queries):
        if query[0] != "?":
            answer.append(trie.starts_with_prefix(query))
            continue

        if query[-1] != "?":
            answer.append(reverse_trie.starts_with_prefix(query[::-1]))
            continue

        answer.append(words_length.count(len(query)))

    return answer


class TestStringMethods(unittest.TestCase):
    def test_example_input(self):
        result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
        self.assertEqual(result, [3, 2, 4, 1, 0])

    def test_reversed_word(self):
        result = solution(["ab"], ["?a"])
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()

# 참고
# https://velog.io/@hope1213/프로그래머스-가사검색-파이썬
