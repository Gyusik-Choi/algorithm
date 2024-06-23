from typing import List
from unittest import TestCase


class Solution:
    def __init__(self):
        self.dp = dict()

    def rob(self, nums: List[int]) -> int:
        def _robbery(n):
            if n in self.dp:
                return self.dp[n]

            if n < 0:
                self.dp[n] = 0
                return self.dp[n]

            self.dp[n] = max(_robbery(n - 1), _robbery(n - 2) + nums[n])
            return self.dp[n]

        return _robbery(len(nums) - 1)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        answer = self.solution.rob([1, 2, 3, 1])
        self.assertEqual(4, answer)

    def test_rob_2(self):
        answer = self.solution.rob([2, 7, 9, 3, 1])
        self.assertEqual(12, answer)

    def test_rob_3(self):
        answer = self.solution.rob([1])
        self.assertEqual(1, answer)

    def test_rob_4(self):
        answer = self.solution.rob([1, 2])
        self.assertEqual(2, answer)

    def test_rob_5(self):
        answer = self.solution.rob([2, 1, 1, 2])
        self.assertEqual(4, answer)

    def test_rob_6(self):
        answer = self.solution.rob([2, 1])
        self.assertEqual(2, answer)
