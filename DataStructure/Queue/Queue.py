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
        if self.is_empty():
            print("queue is empty!")
            return False
        else:
            # 이중 연결리스트 형태라 요소가 1개 일때와 요소가 2개 이상일때로 구분했다.
            # 요소가 1개 일때는 삭제시에 rear 도 아무것도 가리키지 않게 해야한다.
            if self.head.val == self.rear.val:
                self.head = self.head.next
                self.rear = self.head
            # 요소가 2개 이상일 때
            # head 를 head 의 다음 요소로 옮긴 후에
            # 새로운 head 가 기존에 가리키던 prev 를 끊어서 기존의 head 를 더 이상 가리키지 않도록 한다.
            else:
                self.head = self.head.next
                self.head.prev = None
    
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
