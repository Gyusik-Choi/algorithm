import sys
from collections import deque


def bfs(s_y, s_x):
    q = deque([(s_y, s_x, 0)])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    dist_list = []
    visited = [[False] * n for _ in range(n)]
    visited[s_y][s_x] = True
    min_dist = int(1e9)

    while q:
        y, x, dist = q.popleft()
        for k in range(4):
            y_idx = dy[k] + y
            x_idx = dx[k] + x
            if 0 <= y_idx < n and 0 <= x_idx < n and not visited[y_idx][x_idx]:
                if board[y_idx][x_idx] <= shark_size:
                    visited[y_idx][x_idx] = True
                    if 0 < board[y_idx][x_idx] < shark_size:
                        min_dist = dist
                        dist_list.append((dist+1, y_idx, x_idx))
                    if dist + 1 <= min_dist:
                        q.append((y_idx, x_idx, dist+1))

    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark_y = 0
shark_x = 0
shark_size = 2
eat_cnt = 0
fish_cnt = 0
fish_pos = []
time = 0

for i in range(n):
    for j in range(n):
        if 0 < board[i][j] <= 6:
            fish_cnt += 1
            fish_pos.append((i, j))
        elif board[i][j] == 9:
            shark_y, shark_x = i, j

board[shark_y][shark_x] = 0

while fish_cnt:
    result = bfs(shark_y, shark_x)
    if not result:
        break

    shark_y, shark_x = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1

    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0
    board[shark_y][shark_x] = 0

print(time)

# 참고
# https://11001.tistory.com/96
