# 혼동 했던 부분이
# kruskal 은 간선 중심 이라 상관 없다고 생각 했지만
# prim 은 정점 중심 이라 어느 정점을 출발 점으로 두느냐 따라서 값이 달라질 수 있다고 생각 했다
# 그러나 prim 도 어느 정점을 출발 점으로 하든 값은 똑같다
# 비용이 비교적 높은 간선 연결 비용이 모여 있는 정점을 출발 점으로 하면 값이 달라질 수 있다고 혼동 했으나
# 첫 출발점 이후 부터 우선 순위 큐를 통해 비용이 가장 적은 정점을 골라서 이어 나가기 때문에 값은 똑같다
# (임의의 정점을 선택 해서 출발 하므로 첫 출발 점에서 잇는 정점 비용이
# 전체 간선 연결 비용 중 가장 낮은 비용은 아닐 수 있는데 이후 부터는 우선 순위 큐에 의해서
# 가장 작은 간선 연결 비용을 가진 정점이 선택 되게 된다)
# (여기서 선택은 우선 순위 큐에서 꺼내는 heapq.heappop(pq) 해당 코드 부분을 의미 한다)

# 7 11
# 0 5 60
# 0 1 32
# 0 2 31
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51

# 6 10
# 0 1 1
# 0 2 3
# 0 3 2
# 1 2 4
# 1 4 8
# 2 3 5
# 2 4 6
# 2 5 7
# 3 5 10
# 4 5 9

import heapq

V, E = map(int, input().split())
# 인접 리스트 구현 (파일명 'MST_Prim' 에서는 인접 행렬 구현)
adj = {i: [] for i in range(V)}

for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])

# print(adj)
# key, mst, 우선 순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
p = [-1] * V
pq = []

# 시작 정점 선택: 0
key[0] = 0

# 큐에 시작 정점을 넣음 => (key, 정점 index)
# 우선 순위 큐 => heapq 사용
heapq.heappush(pq, (0, 0))  # 우선 순위 큐 => 원소의 첫번째 요소 => key 를 우선 순위로

result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    if mst[node]:
        continue

    # mst 선택
    mst[node] = True
    result += k

    # key 갱신 => key 배열 갱신/ 큐 갱신
    for destination, wt in adj[node]:
        # mst 인지 아닌지 알아야 한다
        if not mst[destination] and key[destination] > wt:
            key[destination] = wt
            p[destination] = node
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요 없는 원소는 스킵
            heapq.heappush(pq, (key[destination], destination))

print(result)
print(p)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=ssarang8649&logNo=220992988177&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
