from unittest import TestCase


class Node:
    def __init__(self, char):
        self.char = char
        self.length = []
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        # "???" 처럼 모두 ? 인 경우에 대비해 head 에도 length 값을 넣어준다
        cur.length.append(len(word))

        for idx, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = Node(char)

            # 단어의 모든 단계마다 length 값을 넣어준다
            # start_with_prefix 에서 하위 노드를 더 탐색하지 않아도 바로 count 를 통해
            # query 조건에 맞는 단어들을 찾을 수 있다
            cur.children[char].length.append(len(word))
            cur = cur.children[char]

    def start_with_prefix(self, prefix):
        cur = self.head

        for idx, p in enumerate(prefix):
            if p == "?":
                break

            if p not in cur.children:
                return 0

            cur = cur.children[p]

        return cur.length.count(len(prefix))


def solution(words, queries):
    trie = Trie()
    reversed_trie = Trie()

    for idx, word in enumerate(words):
        trie.insert(word)
        reversed_trie.insert(word[::-1])

    result = []

    for idx, query in enumerate(queries):
        # 단어가 모두 ? 인 경우
        if query[0] == "?" and query[-1] == "?":
            result.append(trie.start_with_prefix(query))
            continue

        # 단어의 맨 끝이 ? 인 경우
        if query[-1] == "?":
            result.append(trie.start_with_prefix(query))
            continue

        # 단어의 맨 앞이 ? 인 경우
        # 이때는 query 를 뒤집은 값을 인자로 넣어준다
        result.append(reversed_trie.start_with_prefix(query[::-1]))

    return result


class SolutionTest(TestCase):
    def test_solution(self):
        result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
        self.assertEqual([3, 2, 4, 1, 0], result)

    def test_solution2(self):
        result = solution(["abcde", "abc"], ["a??"])
        self.assertEqual([1], result)

    def test_solution3(self):
        result = solution(["abcde"], ["a?"])
        self.assertEqual([0], result)

    def test_solution4(self):
        result = solution(["bcd"], ["a??"])
        self.assertEqual([0], result)

    def test_solution5(self):
        result = solution(["abd", "ace", "bde"], ["??d", "??e", "b??"])
        self.assertEqual([1, 2, 1], result)

    def test_solution6(self):
        result = solution(["abc"], ["???"])
        self.assertEqual([1], result)
