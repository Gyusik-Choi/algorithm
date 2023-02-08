class Node:
    def __init__(self, char, word=None):
        self.one_character = char
        self.word = word
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
        cur.word = word

    def search(self, word):
        cur = self.head
        for w in word:
            if w not in cur.children:
                print("Can't find \"{}\"".format(word))
                return False
            else:
                cur = cur.children[w]

        if cur.word:
            return True
        else:
            print("Can't find \"{}\"".format(word))
            return False

    def starts_with(self, prefix):
        cur = self.head
        for p in prefix:
            if p not in cur.children:
                return False
            else:
                cur = cur.children[p]

        words = []
        words_lst = []
        words_lst.extend(cur.children.values())
        while words_lst:
            cur_node = words_lst.pop(0)
            if cur_node.word:
                words.append(cur_node.word)
            words_lst.extend(cur_node.children.values())

        print(words)
        return words

    def __str__(self):
        words = ""
        cur = self.head
        words_lst = []
        words_lst.extend(cur.children.values())
        while words_lst:
            cur_node = words_lst.pop(0)
            if cur_node.word:
                words += cur_node.word + ", "
            words_lst.extend(cur_node.children.values())

        words = words.rstrip(", ")
        return words


t = Trie()
t.insert("abc")
t.insert("abd")
t.insert("bac")
t.insert("bdc")
t.search("abc")
t.search("def")
t.starts_with("ab")
print(t)
