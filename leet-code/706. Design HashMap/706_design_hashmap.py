from collections import defaultdict


# 키가 충돌하는 경우 연결 리스트로 연결
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hash_map = defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        # 키
        k = key % self.size
        # hash_map 이 dict 가 아닌 defaultdict 라서
        # self.hash_map[k] is None 는
        # 항상 만족하지 못한다
        # 존재하지 않는 key 로 접근할 경우
        # key error 를 발생 시키지 않고
        # 해당 key 를 등록한다
        if self.hash_map[k].value is None:
            self.hash_map[k] = Node(key, value)
            return

        p = self.hash_map[k]

        while p:
            if p.key == key:
                p.value = value
                return

            # p.next 가 None 일 경우
            # p = p.next 로직이 실행되지 않도록 break 한다
            # p.next 에 새 Node 를 등록해야 하는데
            # p 가 None 이 되면 연결 리스트가 끊긴다
            if p.next is None:
                break

            p = p.next

        p.next = Node(key, value)

    def get(self, key: int) -> int:
        k = key % self.size

        if self.hash_map[k].value is None:
            return -1

        p = self.hash_map[k]

        while p:
            if p.key == key:
                return p.value

            p = p.next

        # while 문의 if 문에 걸리지 않았다면
        # 일치하는 key 가 없었다는 뜻이다
        return -1

    def remove(self, key: int) -> None:
        k = key % self.size

        if self.hash_map[k].value is None:
            return

        p = self.hash_map[k]

        # 일치하는 키를 바로 찾음
        if p.key == key:
            if p.next is None:
                # p = Node()
                # 위의 코드는 self.hash_map[k] 를 변화 시키지 않고
                # p 가 보는 대상이 바뀔 뿐이다
                self.hash_map[k] = Node()
            else:
                self.hash_map[k] = p.next
            return

        # prev = p
        #
        # while p:
        #     if p.key == key:
        #         prev.next = p.next
        #         return
        #
        #     prev, p = p, p.next

        # 위의 주석 처리한 코드는 교재의 코드다
        # while 문 안에서 첫번째 if 문은
        # 충족하지 않아서 prev.next, p.next 가
        # 같은 next 를 바라볼 일은 없다
        # 그러나 위의 코드를 바꿔보고 싶어서
        # 아래와 같이 변경했다

        # 일치하는 키를 찾아 나선다
        # 단 첫번째 key 가 아니라
        # 중간에 있는 key 를 찾아 나서기 때문에
        # 해당 키와 연결 관계를 끊고
        # 해당 키의 왼쪽과 오른쪽을 서로 연결해야 한다
        prev, p = p, p.next

        while p:
            if p.key == key:
                prev.next = p.next
                return

            prev, p = p, p.next


hash = MyHashMap()
a = hash.put(1, 1)
b = hash.put(2, 2)
c = hash.get(1)
d = hash.get(3)
e = hash.put(2, 1)
f = hash.get(2)
g = hash.remove(2)
h = hash.get(2)

print(a, b, c, d, e, f, g, h)
