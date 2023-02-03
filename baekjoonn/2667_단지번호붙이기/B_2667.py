def dfs(y, x):
    cnt = 0
    stack = [[y, x]]
    while stack:
        tmp = stack.pop()
        ty = tmp[0]
        tx = tmp[1]
        # 상 우 하 좌
        ay = [1, 0, -1, 0]
        ax = [0, 1, 0, -1]
        for k in range(4):
            dy = ty + ay[k]
            dx = tx + ax[k]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] == 1 and [dy, dx] not in stack and visited[dy][dx] == 0:
                    stack.append([dy, dx])
        visited[ty][tx] = 1
        cnt += 1
    return cnt


N = int(input())
counts = []
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            c = dfs(i, j)
            counts.append(c)

print(len(counts))
counts = sorted(counts)
for i in range(len(counts)):
    print(counts[i])
