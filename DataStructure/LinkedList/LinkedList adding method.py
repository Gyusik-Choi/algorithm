class Node:
    def __init__(self, item, next=None):
        self.val = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.next = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def list_size(self):
        return self.size

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(item)
        self.size += 1

    def print_list(self):
        cur = self.head
        while cur:
            if cur.next is not None:
                print(cur.val, "-> ", end="")
                cur = cur.next
            else:
                print(cur.val)
                cur = cur.next

    def append_left(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            self.head = Node(item, self.head)
        self.size += 1

    def insert(self, item, idx):
        if idx > self.size:
            print("Wrong Index")
        else:
            if self.is_empty():
                self.head = Node(item)
            else:
                if idx == 0:
                    self.head = Node(item, self.head)
                else:
                    cur = self.head
                    i = 0
                    while i + 1 < idx:
                        cur = cur.next
                        i += 1
                    cur.next = Node(item, cur.next)
        self.size += 1

    def delete(self, idx):
        if idx >= self.size:
            print("Wrong Index")
        elif self.is_empty():
            print("Empty")
        else:
            if idx == 0:
                self.head = self.head.next
            else:
                cur = self.head
                i = 0
                while i + 1 < idx:
                    cur = cur.next
                    i += 1
                cur.next = cur.next.next
            self.size -= 1

    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.next.val == item:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
        self.size -= 1

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


ll = LinkedList()
ll.append('A')
ll.print_list()
ll.append_left('B')
ll.print_list()
ll.insert('C', 1)
ll.print_list()
ll.delete(1)
ll.print_list()
ll.append('C')
ll.print_list()
ll.remove('C')
ll.print_list()
ll.append_left('C')
ll.print_list()
ll.reverse()
ll.print_list()

# 참고
# https://underflow101.tistory.com/3?category=826162