def solution(board):
    def get_consecutive_y(start):
        y, x = start[0], start[1]

        for k in range(y + 1, n):
            if board[k][x] == 0:
                return k

        return n

    def get_consecutive_x(start):
        y, x = start[0], start[1]

        for k in range(x + 1, m):
            if board[y][k] == 0:
                return k

        return m

    def is_square(start, end):
        return (end[0] - start[0]) == (end[1] - start[1])

    def get_square_size(start, end):
        return (end[0] - start[0] + 1) * (end[1] - start[1] + 1)

    def set_visited(start, end):
        for y in range(start[0], end[0]):
            for x in range(start[1], end[1]):
                visited[y][x] = True

    def find_max_square_size(start):
        temp_max_square_size = 0
        temp_max_y = start[0]
        temp_max_x = start[1]

        y_max = get_consecutive_y(start)
        y, x = start[0], start[1]

        for k in range(y, y_max):
            x_max = get_consecutive_x([k, x])
            if is_square(start, [k, x_max]):
                temp_max_square_size = max(temp_max_square_size, get_square_size(start, [k, x_max]))
                temp_max_y = k - 1
                temp_max_x = x_max - 1

        set_visited(start, [temp_max_y + 1, temp_max_x + 1])
        return temp_max_square_size

    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    max_square_size = 0

    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if not c:
                continue

            if visited[i][j]:
                continue

            max_square_size = max(max_square_size, find_max_square_size([i, j]))

    return max_square_size


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
