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
        if self.size == 0:
            return True
        return False

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = Node(item)
            cur.next.next = self.head
        self.size += 1

    def append_first(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            cur = self.head
            self.head = Node(item)
            self.head.next = cur
            cur.next = self.head
        self.size += 1

    def insert(self, item, idx):
        if idx > self.size:
            print("Wrong Index")
            return

        if idx == 0:
            if self.is_empty():
                self.head = Node(item)
                self.head.next = self.head
            else:
                cur = self.head
                cur2 = self.head
                self.head = Node(item)
                self.head.next = cur
                while cur2.next is not cur:
                    cur2 = cur2.next
                cur2.next = self.head
        else:
            cur = self.head
            i = 1
            while idx > i:
                cur = cur.next
                i += 1
            original_cur_next = cur.next
            cur.next = Node(item)
            cur.next.next = original_cur_next
        self.size += 1

    def remove(self, item):
        self.size -= 1
        pass

    def print_list(self):
        pass


cll = CircularLinkedList()
cll.append(3)
cll.append_first(2)
cll.insert(1, 0)
cll.insert(4, 3)
cll.append(5)

# 참고
# https://comdoc.tistory.com/entry/%EC%9B%90%ED%98%95-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8Circular-linked-list-ADT-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# http://cis.cju.ac.kr/wp-content/lecture-materials/computer-algorithms/Chapter%2005%20%EC%97%B0%EA%B2%B0%20%EB%A6%AC%EC%8A%A4%ED%8A%B8(Linked%20List)%203.pdf
