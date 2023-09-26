class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [None] * k
        self.size = k
        self.start = 0
        self.end = 0

    def en_queue(self, value: int) -> bool:
        if self.arr[self.end] is not None:
            return False

        self.arr[self.end] = value
        self.end = (self.end + 1) % self.size
        return True

    def de_queue(self) -> bool:
        if self.arr[self.start] is None:
            return False

        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self.arr[self.start]

    def rear(self) -> int:
        return -1 if self.is_empty() else self.arr[(self.end + self.size - 1) % self.size]

    def is_empty(self) -> bool:
        return self.start == self.end and self.arr[self.start] is None

    def is_full(self) -> bool:
        return self.start == self.end and self.arr[self.end] is not None


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3)
a = myCircularQueue.en_queue(1)
b = myCircularQueue.en_queue(2)
c = myCircularQueue.en_queue(3)
d = myCircularQueue.en_queue(4)
e = myCircularQueue.rear()
f = myCircularQueue.is_full()
g = myCircularQueue.de_queue()
h = myCircularQueue.en_queue(4)
i = myCircularQueue.rear()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
