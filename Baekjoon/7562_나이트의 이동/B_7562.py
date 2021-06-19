from collections import deque


def bfs(deq):
    y_axis = [2, 1, -1, -2, -2, -1, 1, 2]
    x_axis = [1, 2, 2, 1, -1, -2, -2, -1]
    while deq:
        y, x = deq.popleft()
        for j in range(8):
            y_location = y + y_axis[j]
            x_location = x + x_axis[j]
            if 0 <= y_location < length and 0 <= x_location < length:
                if y_location == to_move_y and x_location == to_move_x:
                    return chessboard[y][x]
                if not chessboard[y_location][x_location]:
                    chessboard[y_location][x_location] = chessboard[y][x] + 1
                    deq.append([y_location, x_location])


T = int(input())
for _ in range(T):
    length = int(input())
    chessboard = [[0] * length for _ in range(length)]
    cur_y, cur_x = map(int, input().split())
    to_move_y, to_move_x = map(int, input().split())
    chessboard[cur_y][cur_x] = 1
    d = deque()
    d.append([cur_y, cur_x])
    if cur_y == to_move_y and cur_x == to_move_x:
        print(0)
    else:
        print(bfs(d))
