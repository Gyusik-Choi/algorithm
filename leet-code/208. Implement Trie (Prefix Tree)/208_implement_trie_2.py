from collections import defaultdict


class Node:
    def __init__(self):
        self.word = False
        self.children = defaultdict(Node)


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur = self.head

        for w in word:
            cur = cur.children[w]

        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.head

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        return cur.word

    def starts_with(self, prefix: str) -> bool:
        cur = self.head

        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]

        # search 와 달리 True 를 리턴한다
        # search 는
        # word 가 Trie 에 존재 하는지 여부를 판단해야 해서
        # cur.word 가 True 인지 확인한다
        #
        # apple 을 Trie 에 넣었다고 할 때
        # app 을 search 하면
        # app 이라는 단어는 Trie 에 존재하지 않는다
        # 반면에
        # app 을 starts_with 하면
        # app 이 Trie 에 존재 하는지 여부를 판단하는게 아니라
        # app 으로 시작하는 단어가 있는지 여부를 판단해야 해서
        # for 문만 완료할 수 있다면 True 를 리턴하면 된다
        # for 문을 돌면서 not in 연산에 걸리면 False 를 리턴하기 때문에
        # for 문을 완료 했다는 것은
        # app 이 Trie 에 존재 하거나
        # app 으로 시작하는 단어가 존재 한다는 것이다
        return True
