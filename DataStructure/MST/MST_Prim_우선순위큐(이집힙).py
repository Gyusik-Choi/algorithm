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

import heapq

V, E = map(int, input().split())
# 인접리스트로 구현(파일명 'MST_Prim' 에서는 인접행렬로 구현)
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])

# print(adj)
# key, mst, 우선순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
p = [-1] * V
pq = []
# 시작 정점 선택: 0
key[0] = 0
# 큐에 시작 정점을 넣음 => (key, 정점 index)
# 우선순위 큐 => heapq 라이브버리 사용
heapq.heappush(pq, (0, 0))  # 우선순위 큐 => 원소의 첫번째 요소 => key 를 우선순위로
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
        # mst 인지 아닌지 알아야한다
        if not mst[destination] and key[destination] > wt:
            key[destination] = wt
            p[destination] = node
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는 원소는 스킵
            heapq.heappush(pq, (key[destination], destination))

print(result)
print(p)
