from collections import deque


def solution(maps):
    def find_start():
        for i, row in enumerate(maps):
            for j, col in enumerate(row):
                if col == 'S':
                    return [i, j]
        return [-1, -1]

    def find_lever():
        for i, row in enumerate(maps):
            for j, col in enumerate(row):
                if col == 'L':
                    return [i, j]
        return [-1, -1]

    def bfs(start, end_letter):
        # deq = deque([start[0], start[1], 0])
        # 위와 같이 작성하지 않도록 주의
        deq = deque([[start[0], start[1], 0]])

        visit = [[False] * m for _ in range(n)]
        visit[start[0]][start[1]] = True

        y_value = [-1, 0, 1, 0]
        x_value = [0, 1, 0, -1]

        while deq:
            y, x, cnt = deq.popleft()

            for i in range(4):
                y_idx, x_idx = y + y_value[i], x + x_value[i]

                if 0 > y_idx or y_idx >= n or 0 > x_idx or x_idx >= m:
                    continue

                if maps[y_idx][x_idx] == 'X':
                    continue

                if visit[y_idx][x_idx]:
                    continue

                if maps[y_idx][x_idx] == end_letter:
                    return cnt + 1

                visit[y_idx][x_idx] = True
                deq.append([y_idx, x_idx, cnt + 1])

        return -1

    maps = list(map(lambda x: list(x), maps))
    n, m = len(maps), len(maps[0])

    start_to_lever = bfs(find_start(), 'L')

    if start_to_lever == -1:
        return - 1

    lever_to_exit = bfs(find_lever(), 'E')

    if lever_to_exit == -1:
        return -1

    return start_to_lever + lever_to_exit


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
