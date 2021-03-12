class Node:
    def __init__(self, item, prev=None, next=None):
        self.val = item
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)


class Queue:
    def __init__(self):
        # head 에서 삭제, rear 에서 삽입이 발생
        self.head = Node(None)
        self.rear = Node(None, self.head)
        self.head.next = self.rear

    def __str__(self):
        print_queue = '<= ['
        cur = self.head
        while cur:
            print_queue += str(cur.val)
            print_queue += ', '
            cur = cur.next
        print_queue += '] <='
        return print_queue
    
    def is_empty(self):
        if self.head.val is None and self.rear.val is None:
            return True
        else:
            return False

    def en_queue(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.rear = self.head
        else:
            tmp = self.rear
            self.rear = Node(item, tmp)
            tmp.next = self.rear

    # self.head 가 가리키는 노드를 self.head.next 로 바꾼다
    # 기존의 self.head 에 해당하는 노드가 연결고리에서 빠진다
    def de_queue(self):
        if not self.is_empty():
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            tmp.next = None
        else:
            print("queue is empty!")
    
    # 맨 앞의 노드
    def peek(self):
        print(self.head.val)
        return self.head.val
    
    # self.head 를 cur 라는 변수로 받고서
    # cur 가 있는 곳 까지(마지막 노드까지)
    # cur 가 가리키는 노드들을 출력
    def print_list(self):
        cur = self.head
        while cur:
            if cur.next is not None:
                print(cur.val, '<=> ', end='')
            else:
                print(cur.val)
            cur = cur.next


q = Queue()
q.en_queue(1)
q.en_queue(2)
q.en_queue(3)
q.de_queue()
q.print_list()
q.en_queue(4)
q.print_list()
q.peek()
print(q)
# print('de_queue :', q.de_queue())
# print('peek :', q.peek())
# for i in range(10):
#     q.en_queue(i)
# print(q)
