from collections import deque
import sys


def find_k_distance_cities(go):
    distances = [0] * (N + 1)

    visited = [False] * (N + 1)
    visited[go] = True

    deq = deque()
    deq.append(go)

    answer = []

    while deq:
        start = deq.popleft()

        if distances[start] >= K:
            break

        for i, end in enumerate(city[start]):
            if not visited[end]:
                visited[end] = True
                deq.append(end)
                distances[end] = distances[start] + 1

                if distances[end] == K:
                    answer.append(end)

    return answer if len(answer) else [-1]


N, M, K, X = map(int, sys.stdin.readline().split())
city = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    city[A].append(B)

arr = find_k_distance_cities(X)
arr.sort()

for idx, number in enumerate(arr):
    sys.stdout.write(str(number) + "\n")
