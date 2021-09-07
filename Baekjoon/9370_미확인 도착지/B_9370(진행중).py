import sys


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
