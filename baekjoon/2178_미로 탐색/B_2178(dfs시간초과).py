def dfs_recursion(y, x, cnt):
    global min_cnt
    y_axis = [1, 0, -1, 0]
    x_axis = [0, 1, 0, -1]
    for i in range(4):
        y_idx = y + y_axis[i]
        x_idx = x + x_axis[i]
        if 0 <= y_idx < N and 0 <= x_idx < M:
            if y_idx == N - 1 and x_idx == M - 1:
                if min_cnt != 1 and min_cnt > cnt + 1:
                    min_cnt = cnt + 1
                elif min_cnt == 1:
                    min_cnt = cnt + 1
            if maze[y_idx][x_idx] == 1 and visited[y_idx][x_idx] == 0:
                visited[y][x] = 1
                dfs_recursion(y_idx, x_idx, cnt+1)
                visited[y][x] = 0


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
min_cnt = 1
dfs_recursion(0, 0, 1)
print(min_cnt)
