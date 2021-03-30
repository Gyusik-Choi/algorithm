import heapq


V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, v = map(int, input().split())
    adj[s].append([e, v])
    adj[e].append([s, v])

INF = float('inf')
key = [INF] * V
p = [-1] * V
mst = [False] * V

key[0] = 0
heap = []
# 가중치를 기준으로 최소값을 찾아낼 거라 (v, e) 튜플의 앞 요소가 가중치, 뒤가 출발점이다
heapq.heappush(heap, (0, 0))

sums = 0
while heap:
    value, start = heapq.heappop(heap)
    # mst 여부를 체크하여 싸이클이 안생기도록 하며 중복 검사를 막는다
    if mst[start]:
        continue
    mst[start] = True
    sums += value
    for end, val in adj[start]:
        if not mst[end]:
            heapq.heappush(heap, [val, end])
            p[end] = start


print(p)
print(mst)
print(sums)
