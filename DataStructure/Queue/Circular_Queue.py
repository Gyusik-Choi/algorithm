MAX_QSIZE = 10


class CircularQueue:
    def __init__(self):
        self.front = 0
        self.end = 0
        self.items = [None] * MAX_QSIZE

    def is_empty(self):
        return self.front == self.end

    def is_full(self):
        # rear 는 항상 front 보다 앞에 있거나 같다
        # index 는 원형이라 더 작을 수 있지만 rear 를 넘어서 front 가 갈 수는 없다.
        return self.front == (self.end + 1) % MAX_QSIZE

    def clear(self):
        return self.front == self.end

    def length(self):
        return (self.end - self.front + MAX_QSIZE) % MAX_QSIZE

    def enqueue(self, item):
        if not self.is_full():
            self.end = (self.end + 1) % MAX_QSIZE
            self.items[self.end] = item

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def print_queue(self):
        arr = []
        if self.front < self.end:
            arr = self.items[self.front + 1: self.end + 1]
        elif self.front == self.end:
            arr = []
        else:
            arr = self.items[:self.end + 1] + self.items[self.front + 1:]
        print("#{} {} {}".format(self.front, self.end, arr))


cq = CircularQueue()
cq.enqueue(1)
cq.dequeue()
cq.print_queue()
cq.enqueue(2)
cq.dequeue()
cq.print_queue()
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.print_queue()
