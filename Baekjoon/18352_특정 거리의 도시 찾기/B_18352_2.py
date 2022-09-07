from collections import deque
import sys


def bfs(start, dist):
    answer_cities = []

    visited = [False] * (n + 1)
    visited[start] = True
    distances = [0] * (n + 1)

    deq = deque()
    deq.append(start)

    while deq:
        go = deq.popleft()

        if distances[go] >= dist:
            break

        for idx, city in enumerate(roads[go]):
            if not visited[city]:
                deq.append(city)
                visited[city] = True
                distances[city] = distances[go] + 1

                if distances[city] == dist:
                    answer_cities.append(city)

    return answer_cities


n, m, k, x = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    roads[a].append(b)

answer = bfs(x, k)
if not answer:
    sys.stdout.write(str(-1))
else:
    answer.sort()
    for i, a in enumerate(answer):
        sys.stdout.write(str(a) + "\n")
