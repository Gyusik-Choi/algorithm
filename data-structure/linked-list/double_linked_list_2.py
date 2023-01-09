class Node:
    def __init__(self, item, prev=None, next=None):
        self.val = item
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.rear = self.head
        self.size = 0

    def list_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def append_left(self, item):
        if self.is_empty():
            self.head.val = item
            # 아무 요소도 없을 때는 위와 아래가 똑같다
            # self.head = Node(item)
            # self.rear = self.head
        else:
            cur = self.head
            self.head = Node(item)
            self.head.next = cur
            cur.prev = self.head
        self.size += 1

    def append(self, item):
        if self.is_empty():
            self.head.val = item
        else:
            cur = self.rear
            self.rear = Node(item, cur)
            cur.next = self.rear
        self.size += 1

    def insert(self, idx, item):
        if idx < 0 or self.size < idx:
            print("Wrong Index")
            return

        if self.is_empty():
            self.head.val = item
        else:
            if idx == 0:
                cur = self.head
                self.head = Node(item, None, cur)
                cur.prev = self.head
            elif idx > 0 and idx == self.size:
                cur = self.rear
                self.rear = Node(item, cur)
                cur.rear = self.rear
            else:
                # head 에서 더 가까운 경우
                if self.size // 2 >= idx:
                    cur = self.head
                    i = 1
                    while i < idx:
                        cur = cur.next
                        i += 1
                    original_cur_next = cur.next
                    cur.next = Node(item, cur, original_cur_next)
                    original_cur_next.prev = cur.next
                # rear 에서 더 가까운 경우
                else:
                    cur = self.rear
                    i = self.size - 1
                    while idx < i:
                        cur = cur.prev
                        i -= 1
                    original_cur_prev = cur.prev
                    cur.prev = Node(item, cur.prev, cur)
                    original_cur_prev.next = cur.prev
        self.size += 1

    def delete(self, idx):
        if idx < 0 or idx >= self.size or self.size == 0:
            print("Wrong Index")
            return

        if idx == 0:
            if self.size > 1:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head.val = None
        elif idx == self.size - 1:
            self.rear = self.rear.prev
            self.rear.next = None
        else:
            if self.size // 2 >= idx:
                cur = self.head
                i = 1
                while i < idx:
                    cur = cur.next
                    i += 1
                cur.next = cur.next.next
                cur.next.prev = cur
            else:
                cur = self.rear
                i = self.size - 2
                while idx < i:
                    cur = cur.prev
                    i -= 1
                cur.prev = cur.prev.prev
                cur.prev.next = cur
        self.size -= 1

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()


dll = DoubleLinkedList()
dll.is_empty()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.delete(1)
dll.print_list()
