class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node(w)
            cur = cur.children[w]
        cur.data = word

    def search(self, word):
        cur = self.head
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False
        if cur.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        cur = self.head
        result = []
        sub_trie = None

        # 트라이에서 prefix 를 찾고,
        # prefix 의 마지막 글자 노드를 sub_trie 로 설정
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
                subtrie = cur
            else:
                return None

        # bfs 로 prefix sub_trie 를 순회하며
        # data 가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(sub_trie.children.values())

        while queue:
            curr_node = queue.pop()
            if curr_node.data is not None:
                result.append(curr_node.data)

            queue += list(curr_node.children.values())

        return result


t = Trie()
t.insert("abc")
t.insert("abd")
t.insert("abcd")
t.search("ab")
t.search("abcd")
t.starts_with("ab")

# 참고
# https://m.blog.naver.com/cjsencks/221740232900
# https://gist.github.com/osori/29289bc21d453777c5133754e1d5dfd9
