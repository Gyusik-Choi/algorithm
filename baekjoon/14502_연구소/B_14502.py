from collections import deque


def count_zero(v):
    cnt = 0
    for i in range(len(v)):
        for j in range(len(v[i])):
            if v[i][j] == 0:
                cnt += 1

    return cnt


def bfs():
    visited = [[0] * M for _ in range(N)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            visited[i][j] = maps[i][j]

    y_direction = [-1, 0, 1, 0]
    x_direction = [0, 1, 0, -1]

    deq = deque()
    for two in twos:
        deq.append(two)

    while deq:
        [y_idx, x_idx] = deq.popleft()

        for k in range(4):
            y_axis = y_idx + y_direction[k]
            x_axis = x_idx + x_direction[k]

            if 0 <= y_axis < N and 0 <= x_axis < M:
                if visited[y_axis][x_axis] == 0 and [y_axis, x_axis] not in deq:
                    deq.append([y_axis, x_axis])
                    visited[y_axis][x_axis] = 2

    count_sums = count_zero(visited)
    return count_sums


def combinations(num, idx, limit):
    if idx == limit:
        combs.append(temp_comb[:])
    else:
        for n in range(num, zeros_length):
            temp_comb.append(n)
            combinations(n + 1, idx + 1, limit)
            temp_comb.pop()


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 모든 0의 위치를 배열에 담고 이 배열의 인덱스로 조합을 구한다
zeros = []
# 2의 위치
twos = []
for i, m in enumerate(maps):
    for j, m_item in enumerate(m):
        if m_item == 0:
            zeros.append([i, j])
        elif m_item == 2:
            twos.append([i, j])

zeros_length = len(zeros)
combs = []
temp_comb = []
combinations(0, 0, 3)

max_zeros = 0
for comb in combs:
    for c in comb:
        y = zeros[c][0]
        x = zeros[c][1]

        maps[y][x] = 1

    max_zeros = max(max_zeros, bfs())

    for c in comb:
        y = zeros[c][0]
        x = zeros[c][1]

        maps[y][x] = 0

print(max_zeros)
