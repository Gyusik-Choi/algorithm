import heapq
import sys


# 다익스트라로 풀면서 의문점은 사이클을 구하려면 특정 정점에서 어느 정점으로 가는것 뿐만 아니라
# 돌아오는 것도 고려를 해야하는데 이 돌아오는 부분을 어떻게 구해야 할지다.
def dijkstra(go):
    selected = [False] * (V + 1)
    distance = [INF] * (V + 1)

    heap = []

    # 루트가 없을 수 있음
    if routes[go] == list():
        return INF

    # selected[go] = True
    # 위는 해주면 안 된다
    # while 문 안의 if selected[start] 문을 통과할 수 없기 때문이다
    for route in routes[go]:
        e, v = route
        distance[e] = v
        heapq.heappush(heap, (v, e))

    while heap:
        val, start = heapq.heappop(heap)
        if selected[start]:
            continue

        selected[start] = True

        # while 문 위에 설정한 시작점에 바로 걸릴 수 있으니 이에 대한 처리가 필요하다
        # => 출발점에 대한 거리 갱신을 while 문 이전에 미리 수행
        # 그리고 우선순위 큐라서 가장 짧은 거리를 기준으로 구하게 되므로
        # 이후의 값은 거리가 더 길기 때문에 go 로 돌아오는 정점을 찾으면 더 짧은 거리를 찾기 위해 탐색하지 않아도 된다
        if start == go:
            return val

        for route in routes[start]:
            end, value = route
            if distance[end] > distance[start] + value:
                distance[end] = distance[start] + value
                heapq.heappush(heap, (distance[end], end))

    return INF


V, E = map(int, sys.stdin.readline().split())
routes = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    routes[a].append([b, c])

INF = float('inf')
min_val = INF
for i in range(1, V + 1):
    min_val = min(min_val, dijkstra(i))

if min_val == INF:
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(min_val))

# 참고
# https://www.acmicpc.net/source/32109329
