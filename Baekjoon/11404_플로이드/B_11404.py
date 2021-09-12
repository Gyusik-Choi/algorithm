import sys


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

routes = []
for _ in range(m):
    s, e, v = map(int, sys.stdin.readline().split())
    routes.append([s, e, v])

INF = float('inf')
visited = [[INF] * (n + 1) for _ in range(n + 1)]

# 경로 초기화
# 똑같은 경로로 더 큰 비용이 주어질 수 있으므로 주의
for route in routes:
    s, e, v = route[0], route[1], route[2]
    if visited[s][e] != INF:
        if visited[s][e] > v:
            visited[s][e] = v
    else:
        visited[s][e] = v

# 1 -> 1, 2 -> 2 등 자신에서 자신으로 가는 경로는 0으로 만들어놓으면
# 추후에 경로 탐색할때 0보다 작은 경로 값은 나오지 않으므로 조건문을 추가하지 않아도 된다
for i in range(1, n + 1):
    visited[i][i] = 0

# 경로 갱신
# 거쳐가는 경로
# 일케하면 주어진 입력 경로만 탐색하게 된다
# 모든 경로를 탐색해야 해서 일케하면 안된다
# for i in range(1, n + 1):
#     for j in range(len(routes)):
#         start, end, value = routes[j][0], routes[j][1], routes[j][2]
#         if i != start and i != end:
#             if visited[start][i] + visited[i][end] < visited[start][end]:
#                 visited[start][end] = visited[start][i] + visited[i][end]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if visited[j][k] > visited[j][i] + visited[i][k]:
                visited[j][k] = visited[j][i] + visited[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if visited[i][j] == INF:
            sys.stdout.write(str(0) + " ")
        else:
            sys.stdout.write(str(visited[i][j]) + " ")
    sys.stdout.write("\n")
