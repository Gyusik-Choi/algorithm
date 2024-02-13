class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        for i in range(n + 1):
            self.__make_set(i)

    def __make_set(self, x):
        self.parent[x] = x

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px <= py:
            self.parent[py] = px
        else:
            self.parent[px] = py


def solution(n, wires):
    # wires.sort()
    # 위처럼 wires 를 정렬 하고
    # 별도로 path compression 을 하지 않으면 오답이 나온다
    # wires 를 정렬 하지 않고
    # 내부 for 문이 끝난 후
    # 별도로 path compression 을 해야 정답을 구할 수 있다
    min_wire_diff = n

    for i, wire in enumerate(wires):
        disjoint_set = DisjointSet(n)

        for j, w in enumerate(wires):
            v1, v2 = w
            if i != j:
                disjoint_set.union_set(v1, v2)

        # path compression 이 완전히 되지 않아
        # 오답이 나올 수 있어서
        # 내부 for 문이 끝난 후
        # path compression 을 별도로 실행
        for j, w in enumerate(wires):
            v1, v2 = w
            disjoint_set.find_set(v1)
            disjoint_set.find_set(v2)

        min_wire_diff = min(
            min_wire_diff,
            abs(disjoint_set.parent.count(disjoint_set.parent[wire[0]]) - disjoint_set.parent.count(disjoint_set.parent[wire[1]]))
        )

    return min_wire_diff


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# https://school.programmers.co.kr/questions/56193
print(solution(6, [[1, 2], [3, 4], [5, 6], [1, 3], [3, 5]]))
