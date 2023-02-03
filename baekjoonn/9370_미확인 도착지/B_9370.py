import heapq
import sys


def dijkstra(departure):
    distance = [INF] * (n + 1)
    selected = [False] * (n + 1)
    heap = []

    distance[departure] = 0
    heapq.heappush(heap, (distance[departure], departure))

    while heap:
        val, start = heapq.heappop(heap)
        if selected[start]:
            continue

        selected[start] = True
        for end, value in roads[start]:
            if not selected[end]:
                if distance[end] > distance[start] + value:
                    distance[end] = distance[start] + value
                    heapq.heappush(heap, (distance[end], end))

    return distance


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # 교차로, 도로, 목적지
    n, m, t = map(int, sys.stdin.readline().split())
    # 출발지, 사이, 사이
    s, g, h = map(int, sys.stdin.readline().split())

    roads = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        # 사이, 사이, 길이
        a, b, d = map(int, sys.stdin.readline().split())
        roads[a].append([b, d])
        roads[b].append([a, d])

    candidates = []
    for _ in range(t):
        x = int(sys.stdin.readline().rstrip())
        candidates.append(x)

    INF = float('inf')
    g_h_val = 0
    for e, v in roads[g]:
        if e == h:
            g_h_val = v

    s_dijkstra = dijkstra(s)

    # s -> h -> g
    g_dijkstra = dijkstra(g)
    s_h_g_sums = s_dijkstra[h] + g_h_val

    # s -> g -> h
    h_dijkstra = dijkstra(h)
    s_g_h_sums = s_dijkstra[g] + g_h_val

    answer = []
    candidates.sort()
    for candidate in candidates:
        if min(s_h_g_sums + g_dijkstra[candidate], s_g_h_sums + h_dijkstra[candidate]) != INF:
            if min(s_h_g_sums + g_dijkstra[candidate], s_g_h_sums + h_dijkstra[candidate]) == s_dijkstra[candidate]:
                answer.append(str(candidate))

    sys.stdout.write(' '.join(answer) + "\n")
