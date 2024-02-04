from collections import deque
from unittest import TestCase


def solution(maps):
    def find_spot(map_info, spot):
        n, m = len(map_info), len(map_info[0])
        for i in range(n):
            for j in range(m):
                if map_info[i][j] == spot:
                    return [i, j]
        return [-1, -1]

    def is_wall(spot):
        return spot == 'X'

    def bfs(map_info, start, end):
        n, m = len(map_info), len(map_info[0])
        deq = deque([[start[0], start[1], 0]])
        visit = [[False] * m for _ in range(n)]
        visit[start[0]][start[1]] = True
        y_value = [-1, 0, 1, 0]
        x_value = [0, 1, 0, -1]

        while deq:
            y, x, cnt = deq.popleft()

            for i in range(4):
                y_idx = y + y_value[i]
                x_idx = x + x_value[i]

                if 0 > y_idx or y_idx >= n or 0 > x_idx or x_idx >= m:
                    continue

                if is_wall(map_info[y_idx][x_idx]):
                    continue

                if visit[y_idx][x_idx]:
                    continue

                if y_idx == end[0] and x_idx == end[1]:
                    return cnt + 1

                deq.append([y_idx, x_idx, cnt + 1])
                visit[y_idx][x_idx] = True

        return -1

    maps = list(map(lambda x: list(x), maps))
    start_to_lever = bfs(maps, find_spot(maps, 'S'), find_spot(maps, 'L'))

    if start_to_lever == -1:
        return -1

    lever_to_end = bfs(maps, find_spot(maps, 'L'), find_spot(maps, 'E'))

    if lever_to_end == -1:
        return -1

    return start_to_lever + lever_to_end


class SolutionTest(TestCase):
    def test_solution(self):
        self.assertEqual(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]), 16)

    def test_solution2(self):
        self.assertEqual(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]), -1)
