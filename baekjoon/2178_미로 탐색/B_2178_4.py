from collections import deque


def bfs(go):
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    visited = [[False] * M for _ in range(N)]
    visited[go[0]][go[1]] = True

    deq = deque()
    deq.append(go)

    while deq:
        y, x, cnt = deq.popleft()

        if y == N - 1 and x == M - 1:
            return cnt + 1

        for i in range(4):
            y_idx = y + y_value[i]
            x_idx = x + x_value[i]

            if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= M:
                continue

            if maze[y_idx][x_idx] == 0:
                continue

            if visited[y_idx][x_idx]:
                continue

            visited[y_idx][x_idx] = True
            deq.append([y_idx, x_idx, cnt + 1])


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
# y축, x축, 칸
print(bfs([0, 0, 0]))
