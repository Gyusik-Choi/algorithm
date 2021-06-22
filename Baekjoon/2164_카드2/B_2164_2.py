# Queue - Singly Linked List with Tail


class Node:
    def __init__(self, item, nex=None):
        self.val = item
        self.next = nex


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.size = 0

    def is_empty(self):
        if self.head.val is None:
            return True
        return False

    def en_queue(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            cur = self.tail
            self.tail = Node(item)
            cur.next = self.tail
        self.size += 1

    def de_queue(self):
        if self.is_empty():
            print("queue is empty")
            return
        else:
            self.size -= 1
            de_queue_item = 0
            if self.head == self.tail:
                de_queue_item = self.head.val
                self.head = Node(None)
                self.tail = self.head
            else:
                de_queue_item = self.head.val
                self.head = self.head.next
            return de_queue_item

    def get_queue(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr


q = Queue()
N = int(input())
for i in range(1, N + 1):
    q.en_queue(i)

if q.size > 1:
    while True:
        q.de_queue()
        if q.size > 1:
            front_item = q.de_queue()
            q.en_queue(front_item)
        else:
            break

lst = q.get_queue()
print(lst[0])
