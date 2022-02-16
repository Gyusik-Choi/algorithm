import sys


def bellman_ford():
    for i in range(N):
        for j in range(M):
            start = bus_map[j][0]
            end = bus_map[j][1]
            distance = bus_map[j][2]

            if distances[start] != INF and distances[end] > distances[start] + distance:
                distances[end] = distances[start] + distance
                if i == N - 1:
                    return False

    return True


N, M = map(int, sys.stdin.readline().split())
bus_map = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    bus_map.append([A, B, C])

INF = float('inf')
distances = [INF] * (N + 1)
distances[1] = 0

answer = bellman_ford()

if not answer:
    sys.stdout.write(str(-1) + "\n")
else:
    for k in range(2, N + 1):
        if distances[k] == INF:
            sys.stdout.write(str(-1) + "\n")
        else:
            sys.stdout.write(str(distances[k]) + "\n")
