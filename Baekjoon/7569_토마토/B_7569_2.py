from collections import deque
import sys


def find_zero():
    for a in range(H):
        for b in range(N):
            for c in range(M):
                if boxes[a][b][c] == 0:
                    return 1
    return 0


def bfs(locations):
    deq = deque()
    for location in locations:
        deq.append(location)

    # 위, 아래, 앞, 오른, 뒤, 왼
    z_location = [-1, 1, 0, 0, 0, 0]
    y_location = [0, 0, -1, 0, 1, 0]
    x_location = [0, 0, 0, 1, 0, -1]

    # boxes 에 0이 없는 경우도 있다
    # 이때는 while 문이 아예 돌지 않기 때문에 바로 0을 출력할 수 있도록
    # max_days 를 0으로 설정한다
    max_days = 0
    while deq:
        z, y, x, cnt = deq.popleft()
        for m in range(6):
            z_idx = z_location[m] + z
            y_idx = y_location[m] + y
            x_idx = x_location[m] + x
            if 0 <= z_idx < H and 0 <= y_idx < N and 0 <= x_idx < M:
                if boxes[z_idx][y_idx][x_idx] == 0:
                    boxes[z_idx][y_idx][x_idx] = 1
                    deq.append([z_idx, y_idx, x_idx, cnt + 1])
                    max_days = max(max_days, cnt + 1)

    if not find_zero():
        return max_days
    return -1


# 가로, 세로, 상자수
M, N, H = map(int, sys.stdin.readline().split())
one = []
boxes = []
for i in range(H):
    box = []
    for j in range(N):
        a_line_of_box = list(map(int, sys.stdin.readline().split()))
        box.append(a_line_of_box)
        for k in range(M):
            if a_line_of_box[k] == 1:
                one.append([i, j, k, 0])
    boxes.append(box)

answer = bfs(one)
sys.stdout.write(str(answer))
