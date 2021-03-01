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
key = [INF] * V
p = [-1] * V
mst = [False] * V
key[0] = 0
cnt = 0
pq = []
heapq.heappush(pq, (0, 0))
while pq:
    key_val, idx = heapq.heappop(pq)
    if mst[idx]:
        continue
    mst[idx] = True
    for j in adj[idx]:
        end = j[0]
        value = j[1]
        if not mst[end] and key[end] > value + key_val:
            key[end] = value + key_val
            p[end] = idx
            heapq.heappush(pq, (key[end], end))

print(key)
print(p)
print(mst)

# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=ssarang8649&logNo=220992988177&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
