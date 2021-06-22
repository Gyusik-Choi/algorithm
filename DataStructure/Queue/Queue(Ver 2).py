# Queue - Singly Linked List with Tail


class Node:
    def __init__(self, item, nex=None):
        self.val = item
        self.next = nex


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

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

    def de_queue(self):
        if self.is_empty():
            print("queue is empty")
            return
        else:
            if self.head == self.tail:
                self.head = Node(None)
                self.tail = self.head
            else:
                self.head = self.head.next

    def print_queue(self):
        arr = []
        cur = self.head
        if not self.is_empty():
            while cur:
                arr.append(cur.val)
                cur = cur.next
        print(arr)
        return arr


q = Queue()
q.en_queue(1)
q.en_queue(2)
q.en_queue(3)
q.en_queue(4)
q.en_queue(5)
q.de_queue()
q.de_queue()
q.de_queue()
q.de_queue()
q.print_queue()
