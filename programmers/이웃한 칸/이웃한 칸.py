def solution(board, h, w):
    n = len(board)
    cnt = 0
    y_value = [-1, 0, 1, 0]
    x_value = [0, 1, 0, -1]

    for i in range(4):
        y = h + y_value[i]
        x = w + x_value[i]

        if 0 > y or y >= n or 0 > x or x >= n:
            continue

        if board[h][w] == board[y][x]:
            cnt += 1

    return cnt


print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1))
