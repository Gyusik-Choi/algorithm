from collections import deque


def after_bfs():
    global total_distance, fish, shark_size, shark_y, shark_x

    if min_y != max_y and min_x != max_x:
        total_distance += distance[min_y][min_x]
        fish += 1

        if fish == shark_size:
            fish = 0
            shark_size += 1

        sea[min_y][min_x] = 0
        shark_y = min_y
        shark_x = min_x
        return True

    return False


def bfs(y, x):
    global min_distance, min_y, min_x

    distance[y][x] = 0

    deq = deque()
    deq.append([y, x])

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    while deq:
        y_idx, x_idx = deq.popleft()

        for k in range(4):
            y_axis = y_idx + y_direction[k]
            x_axis = x_idx + x_direction[k]

            if 0 <= y_axis < N and 0 <= x_axis < N:
                if distance[y_axis][x_axis] == -1 and sea[y_axis][x_axis] <= shark_size:
                    distance[y_axis][x_axis] = distance[y_idx][x_idx] + 1

                    if sea[y_axis][x_axis] != 0 and sea[y_axis][x_axis] < shark_size:
                        if min_distance > distance[y_axis][x_axis]:
                            min_distance = distance[y_axis][x_axis]
                            min_y = y_axis
                            min_x = x_axis
                        elif min_distance == distance[y_axis][x_axis]:
                            if min_y > y_axis:
                                min_y = y_axis
                                min_x = x_axis
                            elif min_y == y_axis:
                                if min_y > y_axis:
                                    min_y = y_axis
                                    min_x = x_axis

                    deq.append([y_axis, x_axis])


def initialize():
    global min_distance, min_y, min_x

    min_y = N
    min_x = N
    min_distance = max_distance

    for n in range(N):
        for m in range(N):
            distance[n][m] = -1


def find_shark():
    global shark_y, shark_x

    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                shark_y = i
                shark_x = j
                sea[i][j] = 0


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
distance = [[-1] * N for _ in range(N)]

shark_y = N
shark_x = N
min_y = N
min_x = N
max_y = N
max_x = N
shark_size = 2
min_distance = 41
max_distance = 41
total_distance = 0
fish = 0

find_shark()

while True:
    initialize()
    bfs(shark_y, shark_x)
    if not after_bfs():
        break

print(total_distance)
