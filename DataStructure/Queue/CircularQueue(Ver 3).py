class CircularQueue:
    def __init__(self, queue_size):
        self.max_size = queue_size
        self.arr = [0] * self.max_size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    def is_full(self):
        if (self.rear + 1) % self.max_size == self.front:
            return True
        return False

    def en_queue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.max_size
            self.arr[self.rear] = item
        else:
            print("queue is full")
            return

    def de_queue(self):
        if not self.is_empty():
            # self.front += 1
            # idx = self.front % self.max_size
            # item = self.arr[idx]
            # return item
            # 위와 같이 이렇게 하면 안된다
            # self.front 의 인덱스가 정확하게 업데이트 되지 않는다
            self.front = (self.front + 1) % self.max_size
            item = self.arr[self.front]
            return item
        else:
            print("queue is empty")
            return

    def queue_size(self):
        return (self.rear - self.front + self.max_size) % self.max_size

    def print_queue(self):
        lst = []
        if self.front < self.rear:
            lst += self.arr[self.front + 1: self.rear + 1]
        elif self.front == self.rear:
            lst = []
        else:
            lst += self.arr[:self.rear + 1] + self.arr[self.front + 1:]
        print(lst)
        return lst


cq = CircularQueue(10)
cq.en_queue(1)
cq.de_queue()
cq.print_queue()
cq.en_queue(2)
cq.de_queue()
cq.print_queue()
cq.en_queue(3)
cq.en_queue(4)
cq.en_queue(5)
cq.print_queue()
