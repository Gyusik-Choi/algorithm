from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    deq = deque()
    # y, x, 거리
    deq.append([0, 0, 1])

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while deq:
        start = deq.popleft()

        for i in range(4):
            start_y, start_x = start[0] + y_value[i], start[1] + x_value[i]

            if 0 > start_y or start_y >= n or 0 > start_x or start_x >= m:
                continue

            if not maps[start_y][start_x]:
                continue

            if visited[start_y][start_x]:
                continue

            if start_y == n - 1 and start_x == m - 1:
                return start[2] + 1

            visited[start_y][start_x] = True
            deq.append([start_y, start_x, start[2] + 1])

    return -1


print(solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]],
))

print(solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1]],
))
