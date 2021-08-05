from collections import deque
import sys


# tomatoes 돌면서 -1이 아니라 0이 있는지를 찾아야 한다
def check_zero():
    for m in range(N):
        for n in range(M):
            if tomatoes[m][n] == 0:
                return 0
    return 1


# 의문. 여러곳에 토마토가 있을 수 있는데 이들이 동시적으로 익어갈텐데 이를 어떻게 체크해야할지.
def bfs(deq):
    max_days = 0
    y_axis = [-1, 0, 1, 0]
    x_axis = [0, 1, 0, -1]
    while deq:
        y, x, days = deq.popleft()
        for k in range(4):
            y_idx = y_axis[k] + y
            x_idx = x_axis[k] + x
            if 0 <= y_idx < N and 0 <= x_idx < M:
                if tomatoes[y_idx][x_idx] == 0:
                    deq.append([y_idx, x_idx, days + 1])
                    tomatoes[y_idx][x_idx] = days + 1
                    if max_days < days + 1:
                        max_days = days + 1

    return max_days


# 가로, 세로
M, N = map(int, sys.stdin.readline().split())
tomatoes = []
for _ in range(N):
    tomato = list(map(int, sys.stdin.readline().split()))
    tomatoes.append(tomato)

d = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            d.append([i, j, 0])

max_day = bfs(d)
if not check_zero():
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(max_day))
