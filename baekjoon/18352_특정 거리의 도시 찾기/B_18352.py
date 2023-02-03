from collections import deque
import sys


def bfs(k, x):
    answer = []
    visited = [0] * (N + 1)
    deq = deque()
    deq.append(x)

    while deq:
        start = deq.popleft()

        if visited[start] == k:
            answer.append(start)
        elif visited[start] > k:
            break

        for city in cities[start]:
            if not visited[city] and city not in deq:
                visited[city] = visited[start] + 1
                deq.append(city)

        visited[start] = 1

    return answer


N, M, K, X = map(int, sys.stdin.readline().split())
cities = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    cities[A].append(B)

answer_cities = bfs(K, X)
if not len(answer_cities):
    sys.stdout.write(str(-1))
else:
    answer_cities.sort()
    for a in answer_cities:
        sys.stdout.write(str(a) + "\n")
