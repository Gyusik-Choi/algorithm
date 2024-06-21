from unittest import TestCase
from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        return max(nums)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_sub_array(self):
        answer = self.solution.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(6, answer)

    def test_max_sub_array_2(self):
        answer = self.solution.max_sub_array([1])
        self.assertEqual(1, answer)

    def test_max_sub_array_3(self):
        answer = self.solution.max_sub_array([5, 4, -1, 7, 8])
        self.assertEqual(23, answer)
