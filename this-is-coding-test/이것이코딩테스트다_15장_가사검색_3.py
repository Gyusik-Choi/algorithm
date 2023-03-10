class Node:
    def __init__(self, key=None, word=None):
        self.key = key
        self.word = word
        self.length = []
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur = self.head
        # "?????" 처럼 모두 ? 로 구성된 query 의 경우에 대비해
        # self.head.length 에 len(word) 를 넣는다
        cur.length.append(len(word))

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node(w)
                # cur.children[w].length.append(len(word))
            # cur.children[w].length.append(len(word)) 코드는 위의 위치에 있으면 안되고
            # 아래의 위치에 있어야 한다
            # "abc", "abd" 가 있다고 할때
            # 만약에 위의 위치에 있으면
            # "abd" 의 "a", "b' 는 앞선 "abc" 의 "a", "b" 에 의해
            # if w not in cur.children 조건을 충족 못하여
            # if 문에 걸리지 않아서
            # length 에 단어 길이를 추가할 수 없다
            cur.children[w].length.append(len(word))
            cur = cur.children[w]

        cur.word = word

    def find_words(self, word):
        cur = self.head

        for w in word:
            if w != "?":
                if w not in cur.children:
                    return 0
                cur = cur.children[w]
            else:
                break

        return cur.length.count(len(word))


def solution(words, queries):
    trie = Trie()
    reversed_trie = Trie()

    for w in words:
        trie.insert(w)

    reversed_words = list(map(lambda x: x[::-1], words))

    for w in reversed_words:
        reversed_trie.insert(w)

    answer = []

    for q in queries:
        if q[-1] == "?":
            answer.append(trie.find_words(q))
            continue

        q = q[::-1]
        answer.append(reversed_trie.find_words(q))

    return answer


# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
# print(solution(["fro", "front", "frost"], ["?????"]))
# print(solution(["abcde", "abc"], ["abc??"]))
