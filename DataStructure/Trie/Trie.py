class Node:
    def __init__(self, item, data=None):
        self.key = item
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
                print("can't find {}".format(word))
                return False

        if cur.data:
            print("True")
            return True
        else:
            print("can't find {}".format(word))
            return False

    def starts_with(self, prefix):
        cur = self.head
        words = []
        words_lst = []

        for p in prefix:
            if p in cur.children:
                cur = cur.children[p]
            else:
                return False

        words_lst.extend(cur.children.values())
        while words_lst:
            cur_node = words_lst.pop()
            if cur_node.data:
                words.append(cur_node.data)
            words_lst.extend(cur_node.children.values())
        print(words)
        return words

    def __str__(self):
        cur = self.head
        words = ""
        words_lst = []
        words_lst.extend(cur.children.values())
        while words_lst:
            cur_node = words_lst.pop()
            if cur_node.data:
                words += cur_node.data + ", "
            words_lst.extend(cur_node.children.values())
        words = words.rstrip(", ")
        return words


t = Trie()
t.insert("abc")
t.insert("abd")
t.insert("bac")
t.insert("bdc")
t.search("abc")
t.starts_with("ab")
print(t)

# 참고
# https://m.blog.naver.com/cjsencks/221740232900
# https://gist.github.com/osori/29289bc21d453777c5133754e1d5dfd9
# http://cd4761.blogspot.com/2017/02/trie-1.html
