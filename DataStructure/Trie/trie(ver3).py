class Node:
    def __init__(self, item, data=None):
        self.key = item
        self.data = data
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for idx, w in enumerate(word):
            if w not in cur.children:
                cur.children[w] = Node(w)
            cur = cur.children[w]

        cur.data = word

    def search(self, word):
        cur = self.head

        for idx, w in enumerate(word):
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False

        if cur.data is not None and cur.data != word:
            return False

        return True

    def starts_with(self, prefix):
        cur = self.head

        for idx, p in enumerate(prefix):
            if p in cur.children:
                cur = cur.children[p]
            else:
                return False

        words_starts_with_prefix = []
        words_list = cur.children

        for words_key, words_value in words_list.items():
            words = self.dfs(words_value, [])
            words_starts_with_prefix.append(words)

        return words_starts_with_prefix

    def dfs(self, node, words):
        if node.data:
            words.append(node.data)
        else:
            for node_key, node_value in node.children.items():
                self.dfs(node_value, words)
        return words


trie = Trie()
trie.insert('ABC')
trie.insert('BCD')
trie.insert('ACD')
trie.insert('ADG')
print(trie.starts_with('A'))
print(trie.starts_with('AB'))
