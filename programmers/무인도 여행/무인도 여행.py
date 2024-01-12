from collections import deque


def solution(maps):
    # start -> list[int]
    def bfs(start):
        sums = 0
        sums += maps[start[0]][start[1]]
        maps[start[0]][start[1]] = 0

        deq = deque([start])
        y_value = [-1, 0, 1, 0]
        x_value = [0, 1, 0, -1]

        while deq:
            y, x = deq.popleft()

            for k in range(4):
                y_idx = y + y_value[k]
                x_idx = x + x_value[k]

                if 0 > y_idx or y_idx >= n or 0 > x_idx or x_idx >= m:
                    continue

                if not maps[y_idx][x_idx]:
                    continue

                sums += maps[y_idx][x_idx]
                maps[y_idx][x_idx] = 0
                deq.append([y_idx, x_idx])

        return sums

    n, m = len(maps), len(maps[0])
    maps = list(map(lambda row: list(map(lambda r: 0 if r == 'X' else int(r), row)), maps))

    stay = []

    for i, line in enumerate(maps):
        for j, l in enumerate(line):
            if not l:
                continue
            stay.append(bfs([i, j]))

    if not stay:
        return [-1]
    return sorted(stay)


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))
