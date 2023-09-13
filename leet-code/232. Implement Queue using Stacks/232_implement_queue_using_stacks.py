class MyQueue:
    def __init__(self):
        self.arr = []
        self.temp_arr = []

    def push(self, x: int) -> None:
        while self.arr:
            self.temp_arr.append(self.arr.pop())

        self.arr.append(x)

        while self.temp_arr:
            self.arr.append(self.temp_arr.pop())

    def pop(self) -> int:
        return self.arr.pop()

    def peek(self) -> int:
        return self.arr[-1]

    def empty(self) -> bool:
        return not len(self.arr)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
