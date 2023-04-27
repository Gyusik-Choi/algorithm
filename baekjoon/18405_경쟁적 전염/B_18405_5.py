from collections import deque
import sys


def bfs(maps, virus, limit, location):
    deq = deque(sorted(virus, key=lambda x: (x[0], x[1])))

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    while deq:
        cnt, num, y, x = deq.popleft()

        if cnt == limit:
            break

        for k in range(4):
            y_idx, x_idx = y + y_value[k], x + x_value[k]

            if 0 > y_idx or y_idx >= N or 0 > x_idx or x_idx >= N:
                continue

            if maps[y_idx][x_idx]:
                continue

            maps[y_idx][x_idx] = num
            deq.append([cnt + 1, num, y_idx, x_idx])

    return maps[location[0]][location[1]]


N, K = map(int, sys.stdin.readline().split())
map_info = []
virus_info = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    map_info.append(row)

    for j, r in enumerate(row):
        if not r:
            continue

        # cnt, num, y, x
        virus_info.append([0, r, i, j])

S, X, Y = map(int, sys.stdin.readline().split())

print(bfs(map_info, virus_info, S, [X - 1, Y - 1]))
