import sys


def bellman_ford():
    for i in range(N - 1):
        for j in range(M):
            start = routes[j][0]
            end = routes[j][1]
            value = routes[j][2]

            if distance[start] != INF and distance[end] > distance[start] + value:
                distance[end] = distance[start] + value

    for i in range(1):
        for j in range(M):
            start = routes[j][0]
            end = routes[j][1]
            value = routes[j][2]

            if distance[start] != INF and distance[end] > distance[start] + value:
                return False

    return True


# 정점, 간선
N, M = map(int, sys.stdin.readline().split())
routes = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    routes.append([A, B, C])

INF = float('inf')
distance = [INF] * (N + 1)
distance[1] = 0
answer = bellman_ford()

if not answer:
    sys.stdout.write(str(-1) + "\n")
else:
    for k in range(2, N + 1):
        # 갈 수 없는 루트도 존재할 수 있다
        if distance[k] == INF:
            sys.stdout.write(str(-1) + "\n")
        else:
            sys.stdout.write(str(distance[k]) + "\n")
