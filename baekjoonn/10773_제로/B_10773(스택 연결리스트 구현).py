import sys


class Node:
    def __init__(self, item, nex=None):
        self.val = item
        self.next = nex


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.size = 0
        self.sums = 0

    def is_empty(self):
        if not self.size:
            return True
        return False

    def append_num(self, item):
        if not self.is_empty():
            self.head = Node(item, self.head)
        else:
            self.head = Node(item)
        self.size += 1
        self.sums += item

    def pop_num(self):
        num = self.head.val
        self.head = self.head.next
        self.size -= 1
        self.sums -= num
        return num


K = int(input())
stack = Stack()
for i in range(K):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        n = stack.pop_num()
    else:
        stack.append_num(number)

if not stack.size:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(stack.sums))
