from unittest import TestCase


class Solution:
    def fib(self, n: int) -> int:
        memo = [0] * (n + 2)
        memo[1] = 1
        # memo = [0] * (n + 1) 은
        # n이 0일 경우 memo[1] = 1 에서 인덱스 에러가 발생한다
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]


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
