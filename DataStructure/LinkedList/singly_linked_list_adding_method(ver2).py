class Node:
    def __init__(self, item, nex=None):
        self.val = item
        self.next = nex


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def is_empty(self):
        if self.size:
            return False
        return True

    def add(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(item)

        self.size += 1

    def insert(self, item, idx):
        if idx < 0 or idx > self.size:
            print("Wrong Index")
            return

        if idx == 0:
            if self.is_empty():
                self.head = Node(item)
            else:
                self.head = Node(item, self.head)
        elif idx == self.size:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(item)
        else:
            cnt = 0
            cur = self.head
            while cnt < idx - 1:
                cur = cur.next
                cnt += 1
            cur.next = Node(item, cur.next)

        self.size += 1

    def add_left(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            self.head = Node(item, self.head)

        self.size += 1

    def remove_by_idx(self, idx):
        if idx < 0 or idx >= self.size:
            print("Wrong Index")
            return

        if idx == 0:
            self.head = self.head.next
        else:
            cur = self.head
            cnt = 0
            while cnt < idx - 1:
                cur = cur.next
                cnt += 1
            cur.next = cur.next.next

        self.size -= 1

    def print_list(self):
        lst = []
        cur = self.head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        print(lst)
        return lst

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev


sll = SinglyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(4)
sll.add(6)
sll.insert(5, 4)
sll.add_left(0)
sll.print_list()
sll.remove_by_idx(6)
sll.print_list()
sll.reverse()
sll.print_list()
