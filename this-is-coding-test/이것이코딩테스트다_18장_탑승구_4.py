class DisjointSet:
    def __init__(self, n):
        self.p = [0] * n

        for i in range(n):
            self.make_set(i)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px >= py:
            self.p[px] = py
        else:
            self.p[py] = px


def find_max_plane(gate):
    max_plane = 0
    disjoint_set = DisjointSet(G + 1)

    for idx, g in enumerate(gate):
        # 동일한 g 값이 연속으로 나왔을 때
        # 낮은 번호의 탑승구를 이용할 수 있도록
        # find_set 연산 결과 값을 기준으로
        # 도킹할 탑승구를 찾아야 한다
        num = disjoint_set.find_set(g)

        if not num:
            # 문제 조건으로
            # 도킹할 수 없는 비행기가 나오면
            # 공항 운행을 종료 하므로
            # for 문을 끝내야 한다
            return max_plane

        disjoint_set.union_set(num, num - 1)
        max_plane += 1

    return max_plane


G = int(input())
P = int(input())
gate_info = [int(input()) for _ in range(P)]
print(find_max_plane(gate_info))
