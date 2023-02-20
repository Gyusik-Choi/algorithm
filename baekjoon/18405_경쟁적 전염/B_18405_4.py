from collections import deque
import sys


def bfs(q, v_map, stop):
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    while q:
        virus, y, x, sec = q.popleft()

        if sec == stop:
            break

        for k in range(4):
            v_y = y + y_value[k]
            v_x = x + x_value[k]

            if 0 > v_y or v_y >= N or 0 > v_x or v_x >= N:
                continue

            if v_map[v_y][v_x]:
                continue

            v_map[v_y][v_x] = virus
            q.append([virus, v_y, v_x, sec + 1])

    return v_map[X - 1][Y - 1]


N, K = map(int, sys.stdin.readline().split())
virus_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus_info = []

for i, virus_row in enumerate(virus_map):
    for j, v in enumerate(virus_row):
        if v > 0:
            # virus 종류, y, x, 시간
            virus_info.append([v, i, j, 0])

# virus 번호 순서로 bfs 탐색할 수 있도록 정렬
virus_info.sort(key=lambda x: x[0])

deq = deque()

for i, info in enumerate(virus_info):
    deq.append(info)

sys.stdout.write(str(bfs(deq, virus_map, S)))
