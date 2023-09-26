class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [None] * (k + 1)
        self.size = k + 1
        self.start = 0
        self.end = 0

    def en_queue(self, value: int) -> bool:
        if self.is_full():
            return False

        self.end = (self.end + 1) % self.size
        self.arr[self.end] = value
        return True

    def de_queue(self) -> bool:
        if self.is_empty():
            return False

        self.start = (self.start + 1) % self.size
        self.arr[self.start] = None
        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self.arr[(self.start + 1) % self.size]

    def rear(self) -> int:
        return -1 if self.is_empty() else self.arr[self.end]

    def is_empty(self) -> bool:
        return self.start == self.end

    def is_full(self) -> bool:
        return (self.end + 1) % self.size == self.start


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

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
print(myCircularQueue.front())
