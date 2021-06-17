class CircularQueue:
    MAX_QSIZE = 10

    def __init__(self):
        self.front = 0
        self.end = 0

        # http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-3-%ED%81%B4%EB%9E%98%EC%8A%A4-%EB%B3%80%EC%88%98class-variable/
        # max_size 를 클래스 변수로 선언했지만 클래스 변수로도 참조가능하고 self 를 사용해서 인스턴스 변수로도 참조 가능하다
        # 실제로는 self 로 선언해서 인스턴수 변수로 참조했다기 보다는
        # 파이썬의 네임스페이스에서 이름을 찾을 때 인스턴스 변수 -> 클래스 변수 -> 수퍼 클래스 변수의 순서로 찾는다
        # self 를 통해서 인스턴스 변수의 네임스페이스를 봤더니 없어서 클래스 변수의 네임스페이스에서 찾은 것이다
        # self.items = [None] * CircularQueue.MAX_QSIZE
        self.items = [None] * self.MAX_QSIZE

    def is_empty(self):
        return self.front == self.end

    def is_full(self):
        # rear 는 항상 front 보다 앞에 있거나 같다
        # index 는 원형이라 더 작을 수 있지만 rear 를 넘어서 front 가 갈 수는 없다.
        return self.front == (self.end + 1) % self.MAX_QSIZE

    def clear(self):
        return self.front == self.end

    def length(self):
        return (self.end - self.front + self.MAX_QSIZE) % self.MAX_QSIZE

    def enqueue(self, item):
        if not self.is_full():
            self.end = (self.end + 1) % self.MAX_QSIZE
            self.items[self.end] = item

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.MAX_QSIZE
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
