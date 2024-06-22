from unittest import TestCase


class Solution:
    def __init__(self):
        self.memo = dict()

    def climb_stairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n < 3:
            self.memo[n] = n
        else:
            self.memo[n] = self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

        return self.memo[n]


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climb_stairs(self):
        answer = self.solution.climb_stairs(2)
        self.assertEqual(2, answer)

    def test_climb_stairs_2(self):
        answer = self.solution.climb_stairs(3)
        self.assertEqual(3, answer)

    def test_climb_stairs_3(self):
        answer = self.solution.climb_stairs(5)
        self.assertEqual(8, answer)
