from collections import deque


def solution(rectangle, character_x, character_y, item_x, item_y):
    def mark_rectangle():
        for rec in rectangle:
            x_1, y_1, x_2, y_2 = rec
            for i in range(y_1, y_2 + 1):
                for j in range(x_1, x_2 + 1):
                    if y_1 < i < y_2 and x_1 < j < x_2:
                        matrix[i][j] = 0
                    else:
                        if matrix[i][j] != 0:
                            matrix[i][j] = 1
                        else:
                            matrix[i][j] = 0

    def bfs():
        y_value = [-1, 0, 1, 0]
        x_value = [0, 1, 0, -1]

        visit = [[0] * 101 for _ in range(101)]
        visit[character_y][character_x] = 1
        deq = deque([[character_y, character_x, 0]])

        while deq:
            y, x, cnt = deq.popleft()

            if y == item_y and x == item_x:
                return cnt // 2

            for i in range(4):
                y_idx, x_idx = y + y_value[i], x + x_value[i]

                if y_idx <= 0 or y_idx >= 101 or x_idx <= 0 or x_idx >= 101:
                    continue

                if visit[y_idx][x_idx]:
                    continue

                if matrix[y_idx][x_idx] != 1:
                    continue

                visit[y_idx][x_idx] = 1
                deq.append([y_idx, x_idx, cnt + 1])

    for idx, r in enumerate(rectangle):
        rectangle[idx] = list(map(lambda x: x * 2, r))
    character_x *= 2
    character_y *= 2
    item_x *= 2
    item_y *= 2

    matrix = [[-1] * 101 for _ in range(101)]
    mark_rectangle()
    answer = bfs()
    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
# print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
# print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
# print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
# print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
