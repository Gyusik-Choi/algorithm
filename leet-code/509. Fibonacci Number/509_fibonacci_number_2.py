from unittest import TestCase


class Solution:
    def __init__(self):
        self.memo = dict()

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n <= 1:
            self.memo[n] = n
            return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


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
