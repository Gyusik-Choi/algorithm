from collections import deque


def bfs(y_location, x_location, cnt):
    global min_cnt
    deq = deque()
    deq.append([y_location, x_location, cnt])
    while deq:
        y, x, c = deq.popleft()
        y_axis = [1, 0, -1, 0]
        x_axis = [0, 1, 0, -1]
        for i in range(4):
            y_idx = y + y_axis[i]
            x_idx = x + x_axis[i]
            if 0 <= y_idx < N and 0 <= x_idx < M:
                if y_idx == N - 1 and x_idx == M - 1:
                    min_cnt = c + 1
                    return

                elif visited[y_idx][x_idx] == 0 and maze[y_idx][x_idx] == 1 and [y_idx, x_idx, c + 1] not in deq:
                    deq.append([y_idx, x_idx, c + 1])
                    visited[y_idx][x_idx] = 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
min_cnt = 1
bfs(0, 0, 1)
print(min_cnt)
