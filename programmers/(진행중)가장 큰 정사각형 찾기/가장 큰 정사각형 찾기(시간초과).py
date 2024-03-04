from collections import deque


def solution(board):
    def is_square(start, end):
        return (end[0] - start[0]) == (end[1] - start[1])

    def get_square_size(start, end):
        return (end[0] - start[0] + 1) * (end[1] - start[1] + 1)

    def get_max_square_size(start):
        temp_max_square_size = 0
        deq = deque([start])

        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True
        # 우, 하
        y_value = [0, 1]
        x_value = [1, 0]

        while deq:
            y, x = deq.popleft()

            for k in range(2):
                y_idx, x_idx = y + y_value[k], x + x_value[k]

                if 0 > y_idx or y_idx >= n or 0 > x_idx or x_idx >= m:
                    continue

                if visited[y_idx][x_idx]:
                    continue

                if board[y_idx][x_idx] == 0:
                    continue

                if is_square(start, [y_idx, x_idx]):
                    temp_max_square_size = max(temp_max_square_size, get_square_size(start, [y_idx, x_idx]))

                deq.append([y_idx, x_idx])
                visited[y_idx][x_idx] = True

        return temp_max_square_size

    max_square_size = 1
    n, m = len(board), len(board[0])

    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if not c:
                continue

            max_square_size = max(max_square_size, get_max_square_size([i, j]))

    return max_square_size


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
