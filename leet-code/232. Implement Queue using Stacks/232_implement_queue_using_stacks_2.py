class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output 에 input 의 요소들을 역순으로 담기 때문에
        # output 에 요소가 남아 있으면
        # 이전에 output 에 들어온 요소들이 있다는 것이다
        # 즉 output 에서 pop 으로 제거할 요소들이 이미 있기 때문에
        # input 을 비워서 output 에 역순으로 넣지 않는다
        #
        # 만약에 output 이 비었다면
        # pop 이나 peek 에서 꺼낼 요소가 없다는 의미라
        # 새로 output 을 채워야 한다
        # 그래서 input 의 모든 요소들을 pop 으로 꺼내서
        # output 에 넣는다
        #
        # output 이 있으면
        # output 에서 pop 으로 꺼내고
        # output 이 비었다면
        # output 에 남은 요소들을 pop 으로 꺼낸다
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
myQueue = MyQueue()
print(myQueue)
print(myQueue.push(1))
print(myQueue.push(2))
print(myQueue.push(3))
print(myQueue.pop())
print(myQueue.push(4))
print(myQueue.push(5))
print(myQueue.pop())
