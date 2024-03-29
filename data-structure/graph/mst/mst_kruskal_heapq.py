# 의문: 프림은 무방향 기준으로 s, e 기준으로 각각 입력을 받았는데 왜 크루스칼 에서는 s 기준으로 한번만 입력받는지
# 생각: 프림과 크루스칼 둘 다 무방향 그래프다. 다만 차이는 프림은 정점을 기준으로, 크루스칼은 간선을 기준으로 탐색이 진행된다.
# 정점을 기준으로 하면 무방향이라 어느 정점을 기준으로 볼 지 모르므로 0, 2, 20을 0에서 2가 20, 2에서 0이 20 둘다 고려해야 한다.
# 반면에 간선을 기준으로 하면 0, 2, 20은 0에서 2가 20, 2에서 0이 20 어차피 똑같이 0과 2를 연결하는 20이기 때문에 두번 볼 필요가 없다.
import heapq


def union(x, y):
    px = find_set(x)
    py = find_set(y)
    p[py] = px


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def make_set(x):
    p[x] = x


V, E = map(int, input().split())
adj = []
for i in range(E):
    s, e, v = map(int, input().split())
    # 최소 가중치를 기준으로 heap 이 정렬되도록 v를 맨 앞에 넣어준다
    adj.append((v, s, e))
heap = []
for item in adj:
    heapq.heappush(heap, item)

# 간선의 갯수(정점의 갯수 - 1)
cnt = 0
# disjoint-set 배열
p = [0] * V
for i in range(V):
    make_set(i)

sums = 0
mst = []
while heap:
    value, start, end = heapq.heappop(heap)
    if find_set(start) == find_set(end):
        continue
    sums += value
    mst.append([start, end])
    union(start, end)

print(sums)
print(mst)

# 참고
# https://blog.naver.com/ssarang8649/221038259400
