import heapq
import sys


def dijkstra(go):
    inf = float('inf')
    distances = [inf] * (n + 1)
    selected = [False] * (n + 1)

    heap = []
    distances[go] = 0
    heapq.heappush(heap, (distances[go], go))

    while heap:
        distance, start = heapq.heappop(heap)

        if selected[start]:
            continue

        selected[start] = True

        for end, dist in roads[start]:
            if not selected[end]:
                if distances[end] > distances[start] + dist:
                    distances[end] = distances[start] + dist
                    heapq.heappush(heap, (distances[end], end))

    return distances


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    roads = {i: [] for i in range(n + 1)}
    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        roads[a].append([b, d])
        roads[b].append([a, d])

    candidates = []
    for i in range(t):
        x = int(sys.stdin.readline().rstrip())
        candidates.append(x)

    # 출발점에서 g/ g 에서 h/ h에서 후보
    # 출발점에서 h/ h 에서 g/ g에서 후보
    from_s = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)

    destinations = []

    for candidate in candidates:
        case1 = from_s[g] + from_g[h] + from_h[candidate]
        case2 = from_s[h] + from_h[g] + from_g[candidate]

        min_case = min(case1, case2)
        # float('inf') 일 경우를 제거해야 한다
        if min_case != float('inf') and min_case == from_s[candidate]:
            destinations.append(candidate)

    destinations.sort()
    for idx, destination in enumerate(destinations):
        sys.stdout.write(str(destination) + " ")
    print()
