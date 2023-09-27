# 배열로 구현하는 큐
# 연결 리스트로 큐를 구현 했었는데
# 연결 리스트로 구현한 큐와 달리
# 크기가 정해져 있다
# 동적으로 크기를 바꿀 수 없어서
# 큐에 요소를 넣었다 뺐더라도
# 한 번 넣은 위치에 다시 넣을 수 없다
# 맨 마지막 위치까지 요소가 들어가면
# 이전 요소들을 뺐는지 여부와 관계없이
# 큐가 가득 차서 더 이상 넣을 수 없다
# 큐의 요소를 앞으로 이동 하려면
# 모든 요소를 앞으로 이동해야 해서
# O(N) 의 시간 복잡도가 발생한다
# 왜 앞으로 요소를 이동할 수 없는 건지
# 처음에는 이해가 잘 되지 않았다
# 사실 이동을 못 한다기 보다는
# 시간 복잡도가 증가 하기 때문에
# 하지 않는 것이라고 봐야 한다
#
# C 언어로 정수 배열을 생성 했다고 하면
# 이 정수 배열의 변수는 (포인터 변수로 선언하지 않았지만)
# 배열의 첫번째 인덱스 주소를 가리킨다
# 그리고 배열의 각 요소를
# 연속된 메모리 공간에 할당한다
# 4바이트(int 크기) * 배열 크기 만큼의
# 연속된 메모리 공간을 갖는다
# 각 요소 마다 메모리 주소가 고정되어 있어서
# 이 배열의 맨 앞 요소를 제거하고
# 나머지 요소들을 앞으로 이동 한다면
# 각 메모리 주소에 모두 새로운 값을 등록해야 한다
# 이를 위해 O(N) 의 시간 복잡도가 발생하기 때문에
# 고정된 크기의 선형 큐는 공간을 재사용할 수 없다

class Queue:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.start = 0
        self.end = 0

    def push(self, value):
        if self.is_full():
            return

        self.arr[self.end] = value
        self.end += 1

    def pop(self):
        if self.is_empty():
            return

        num = self.arr[self.start]
        self.arr[self.start] = None
        self.start += 1
        return num

    def front(self):
        if self.is_empty():
            return None

        if self.start >= self.size:
            return self.arr[self.start - 1]

        return self.arr[self.start]

    def rear(self):
        if self.is_empty():
            return None

        return self.arr[self.end - 1]

    def is_empty(self):
        return self.start == self.end

    def is_full(self) -> bool:
        return self.end >= self.size

# 참고
# https://jhnyang.tistory.com/329
# https://eunjinii.tistory.com/59
