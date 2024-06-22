from unittest import TestCase


class Solution:
    def climb_stairs(self, n: int) -> int:
        if n < 3:
            return n

        fib = [0] * (n + 1)
        fib[1] = 1
        fib[2] = 2

        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]


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
