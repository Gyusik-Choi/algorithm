# 원형 데크를 구현하는 문제지만
# 배열이 아니라 (이중) 연결 리스트로 구현할 예정이라
# 원형일 필요가 없다
# 배열로 큐를 구현할 때 원형 큐를 사용하는 이유는
# 뒤쪽에 요소가 다 차서 더 이상 넣을 수 없는데
# 앞쪽에 빈 공간이 있으면 맨 앞과 맨 뒤를 연결해서
# 앞쪽에 요소를 넣기 위해서다
# 연결 리스트는 배열과 달리 빈 공간이 존재하지 않고
# 데크는 맨 앞과 맨 뒤로 요소를 넣고 빼는 연산이 있지만
# 맨 뒤의 다음 요소를 빼는 등의 연산은 없어서
# 원형으로 구현할 필요가 없다

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = Node(None), Node(None)
        self.size, self.len = k, 0
        # Node(None) <-> Node(None)
        self.head.right, self.tail.left = self.tail, self.head

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        self.len += 1
        self._add(self.head, Node(value))
        return True

    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False
        self.len += 1
        self._add(self.tail.left, Node(value))
        return True

    def _add(self, node: Node, new_node: Node):
        old = node.right
        node.right = new_node
        new_node.left = node
        new_node.right = old
        old.left = new_node

    def delete_front(self) -> bool:
        if self.is_empty():
            return False
        self.len -= 1
        self._delete(self.head)
        return True

    def delete_last(self) -> bool:
        if self.is_empty():
            return False
        self.len -= 1
        self._delete(self.tail.left.left)
        return True

    def _delete(self, node: Node):
        new_right = node.right.right
        node.right = new_right
        new_right.left = node

    def get_front(self) -> int:
        if self.is_empty():
            return -1
        return self.head.right.value

    def get_rear(self) -> int:
        if self.is_empty():
            return -1
        return self.tail.left.value

    def is_empty(self) -> bool:
        return self.len == 0

    def is_full(self) -> bool:
        return self.size == self.len

# 참고
# 파이선 알고리즘 인터뷰
deq = MyCircularDeque(3)
a = deq.insert_last(1)
b = deq.insert_last(2)
c = deq.insert_last(3)
d = deq.insert_last(4)
e = deq.get_rear()
f = deq.is_full()
g = deq.delete_last()
h = deq.insert_front(4)
i = deq.get_front()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
