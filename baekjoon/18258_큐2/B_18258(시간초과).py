import sys


class Node:
    def __init__(self, item, prev=None, next=None):
        self.val = item
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.rear = self.head
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def en_queue(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.rear = self.head
        else:
            cur = self.rear
            self.rear = Node(item, cur)
            cur.next = self.rear
        self.size += 1

    def de_queue(self):
        if self.is_empty():
            return False
        else:
            self.size -= 1
            if self.head.val == self.rear.val:
                cur = self.head
                self.head = self.head.next
                self.rear = self.head
                return cur.val
            else:
                cur = self.head
                self.head = self.head.next
                self.head.prev = None
                return cur.val

    def front_num(self):
        return self.head.val

    def back_num(self):
        return self.rear.val


N = int(input())
q = Queue()
for i in range(N):
    order = sys.stdin.readline().strip()
    if "push" in order:
        order, num = order.split()
        num = int(num)
        q.en_queue(num)
    else:
        if order == 'front':
            if not q.is_empty():
                front_num = q.front_num()
                sys.stdout.write(str(front_num) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        elif order == 'back':
            if not q.is_empty():
                back_num = q.back_num()
                sys.stdout.write(str(back_num) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
        elif order == 'size':
            sys.stdout.write(str(q.size) + "\n")
        elif order == 'empty':
            if q.is_empty():
                sys.stdout.write(str(1) + "\n")
            else:
                sys.stdout.write(str(0) + "\n")
        # pop
        else:
            if not q.is_empty():
                pop_num = q.de_queue()
                sys.stdout.write(str(pop_num) + "\n")
            else:
                sys.stdout.write(str(-1) + "\n")
