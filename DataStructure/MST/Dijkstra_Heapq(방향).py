# 6 11
# 0 1 3
# 0 2 5
# 1 2 2
# 1 3 6
# 2 1 1
# 2 3 4
# 2 4 6
# 3 4 2
# 3 5 3
# 4 0 3
# 4 5 6

import heapq


V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, v = map(int, input().split())
    adj[s].append([e, v])

INF = float('inf')
distance = [INF] * V
selected = [False] * V

distance[0] = 0
heap = []
heapq.heappush(heap, (0, 0))

while heap:
    # 가중치 가장 작은 노드 찾기
    start_value, start = heapq.heappop(heap)
    if selected[start]:
        continue
    selected[start] = True
    # 인접 노드들의 최소거리 업데이트
    for end, value in adj[start]:
        if not selected[end] and distance[end] > distance[start] + value:
            distance[end] = distance[start] + value
            # (거리, 도착점)의 거리를 넣을 때 value 를 넣지 않도록 주의(Prim 과 혼동하지 말 것)
            # 거리에는 업데이트된 거리 값을 넣어줘야 한다
            heapq.heappush(heap, (distance[end], end))

print(distance)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=ssarang8649&logNo=220992988177&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
