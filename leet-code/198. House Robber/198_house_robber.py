from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)


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
