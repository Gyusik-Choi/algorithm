from collections import deque
import sys


def bfs():
    go = []

    for i, map_row in enumerate(maps):
        for j, map_item in enumerate(map_row):
            if maps[i][j] != 0:
                go.append([i, j, maps[i][j], 0])

    go.sort(key=lambda x: x[2])
    deq = deque(go)

    # 위의 deq 는 deque 를 초기화 하면서 2차원 배열을 그대로 넣는다
    # 아래의 deq 는 deque 를 초기화 한 후에 2차원 배열의 요소를 하나씩 꺼내서 넣는다
    # 위와 아래의 deq 는 값을 넣는 방식이 다른데 값은 서로 같다
    # deq = deque()
    # for g in go:
        # deq.append(g)

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    while deq:
        [y_idx, x_idx, value, cnt] = deq.popleft()

        if cnt == S:
            break

        for k in range(4):
            y_axis = y_idx + y_direction[k]
            x_axis = x_idx + x_direction[k]

            if 0 <= y_axis < N and 0 <= x_axis < N:
                if maps[y_axis][x_axis] == 0:
                    maps[y_axis][x_axis] = value
                    deq.append([y_axis, x_axis, value, cnt + 1])


N, K = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, Y, X = map(int, sys.stdin.readline().split())

bfs()
sys.stdout.write(str(maps[Y - 1][X - 1]))
