class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.size = 0

    def is_empty(self):
        pass

    def append(self, item):
        pass

    def append_first(self, item):
        pass

    def insert(self, item, idx):
        self.size += 1
        pass

    def remove(self, item):
        self.size -= 1
        pass

    def print_list(self):
        pass


cll = CircularLinkedList()
cll.print_list()

# 참고
# https://comdoc.tistory.com/entry/%EC%9B%90%ED%98%95-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8Circular-linked-list-ADT-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# http://cis.cju.ac.kr/wp-content/lecture-materials/computer-algorithms/Chapter%2005%20%EC%97%B0%EA%B2%B0%20%EB%A6%AC%EC%8A%A4%ED%8A%B8(Linked%20List)%203.pdf