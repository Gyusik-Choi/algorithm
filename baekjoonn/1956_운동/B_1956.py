import sys


def find_smallest_cycle():
    smallest_cycle = INF
    for o in range(1, V + 1):
        for p in range(1, V + 1):
            if o != p:
                if distance[o][p] != INF and distance[p][o] != INF:
                    smallest_cycle = min(smallest_cycle, distance[o][p] + distance[p][o])
    return smallest_cycle


def floyd_warshall():
    for k in range(V + 1):
        for m in range(V + 1):
            for n in range(V + 1):
                distance[m][n] = min(distance[m][k] + distance[k][n], distance[m][n])


V, E = map(int, sys.stdin.readline().split())
routes = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    routes.append([a, b, c])

# 다익스트라처럼 특정 출발점을 기준으로 최단 거리를 찾는게 아니라
# 전체 경로중 최단 거리를 찾아야하므로 플로이드-워셜 알고리즘을 사용해야 한다

INF = float('inf')
distance = [[INF] * (V + 1) for _ in range(V + 1)]

for route in routes:
    start, end, value = route
    if distance[start][end] != INF:
        if distance[start][end] > value:
            distance[start][end] = value
    else:
        distance[start][end] = value

for i in range(1, V + 1):
    distance[i][i] = 0

floyd_warshall()
answer = find_smallest_cycle()
if answer == INF:
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(answer))

# 참고
# https://jow1025.tistory.com/146
# https://steady-coding.tistory.com/101
