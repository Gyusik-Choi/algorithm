from collections import deque


def solution(board):
    def find_start():
        for i, b in enumerate(board):
            for j, char in enumerate(b):
                if char == 'R':
                    return [i, j]

    def move(y, x, y_val, x_val):
        while True:
            y += y_val
            x += x_val

            if (0 > y or
                    y >= n or
                    0 > x or
                    x >= m or
                    board[y][x] == 'D'):
                break

        # y, x 는 장애물 혹은 보드를 벗어난 위치에 있다
        # 직전 값으로 돌린다
        return [y - y_val, x - x_val]

    def bfs(go):
        deq = deque([[0, go[0], go[1]]])
        visited = [[0] * m for _ in range(n)]
        y_value = [-1, 0, 1, 0]
        x_value = [0, 1, 0, -1]

        while deq:
            dist, y, x = deq.popleft()

            if board[y][x] == 'G':
                return dist

            for i in range(4):
                y_idx, x_idx = move(y, x, y_value[i], x_value[i])

                if visited[y_idx][x_idx]:
                    continue

                visited[y_idx][x_idx] = True
                deq.append([dist + 1, y_idx, x_idx])

        return -1

    board = list(map(lambda x: list(x), board))
    n, m = len(board), len(board[0])
    return bfs(find_start())


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))

# 참고
# https://velog.io/@gale4739/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A6%AC%EC%BD%94%EC%B3%87-%EB%A1%9C%EB%B4%87
