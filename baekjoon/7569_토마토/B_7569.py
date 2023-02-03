from collections import deque


def bfs(deq):
    # 상, 우, 하, 좌, 위, 아래
    z_axis = [0, 0, 0, 0, -1, 1]
    y_axis = [-1, 0, 1, 0, 0, 0]
    x_axis = [0, 1, 0, -1, 0, 0]

    while deq:
        z, y, x = deq.popleft()
        for l in range(6):
            z_idx = z + z_axis[l]
            y_idx = y + y_axis[l]
            x_idx = x + x_axis[l]

            if 0 <= z_idx < H and 0 <= y_idx < N and 0 <= x_idx < M:
                if boxes[z_idx][y_idx][x_idx] == 0:
                    deq.append([z_idx, y_idx, x_idx])
                    boxes[z_idx][y_idx][x_idx] = boxes[z][y][x] + 1

    days = -1
    for floor in boxes:
        for box in floor:
            for b in box:
                if b == 0:
                    return -1
                days = max(days, b)
    return days - 1


M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

d = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                d.append([i, j, k])

ans = bfs(d)
print(ans)
