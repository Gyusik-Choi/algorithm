import sys


def bellman_ford():
    for i in range(N - 1):
        for j in range(M):
            start = bus_route[j][0]
            end = bus_route[j][1]
            time = bus_route[j][2]
            if bf[start - 1] != INF and bf[end - 1] > bf[start - 1] + time:
                bf[end - 1] = bf[start - 1] + time

    # 음의 순환 검사
    for i in range(1):
        for j in range(M):
            start = bus_route[j][0]
            end = bus_route[j][1]
            time = bus_route[j][2]
            if bf[start - 1] != INF and bf[end - 1] > bf[start - 1] + time:
                return -1


N, M = map(int, sys.stdin.readline().split())
bus_route = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    bus_route.append([A, B, C])

INF = float('inf')
bf = [INF] * N
bf[0] = 0

answer = bellman_ford()
if answer == -1:
    sys.stdout.write(str(-1) + "\n")
else:
    for i in range(1, N):
        if bf[i] == INF:
            sys.stdout.write(str(-1) + "\n")
        else:
            sys.stdout.write(str(bf[i]) + "\n")
