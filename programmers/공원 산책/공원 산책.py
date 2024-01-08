from unittest import TestCase


def solution(park, routes):
    def find_start(p):
        for i, r in enumerate(p):
            for j, c in enumerate(r):
                if c == 'S':
                    return [i, j]

    def move(end, park_map):
        h, w = len(park_map), len(park_map[0])
        origin_y, origin_x = find_start(park)
        y, x = origin_y, origin_x
        op, n = end.split()
        n = int(n)

        for _ in range(n):
            if op == 'N':
                y -= 1
            elif op == 'S':
                y += 1
            elif op == 'W':
                x -= 1
            else:
                x += 1

            if y < 0 or y >= h or x < 0 or x >= w:
                return

            if park_map[y][x] == 'X':
                return

        park_map[origin_y][origin_x] = 'O'
        park_map[y][x] = 'S'

    park = list(map(lambda x: list(x), park))

    for route in routes:
        move(route, park)

    return find_start(park)


class TestSolution(TestCase):
    def test_solution(self):
        s = solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])
        self.assertEqual(s, [2, 1])

    def test_solution2(self):
        s = solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"])
        self.assertEqual(s, [0, 1])

    def test_solution3(self):
        s = solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"])
        self.assertEqual(s, [0, 0])
