from unittest import TestCase


class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fib(self):
        answer = self.solution.fib(2)
        self.assertEqual(1, answer)

    def test_fib_2(self):
        answer = self.solution.fib(3)
        self.assertEqual(2, answer)

    def test_fib_3(self):
        answer = self.solution.fib(4)
        self.assertEqual(3, answer)
