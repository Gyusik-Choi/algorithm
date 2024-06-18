from unittest import TestCase


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


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
