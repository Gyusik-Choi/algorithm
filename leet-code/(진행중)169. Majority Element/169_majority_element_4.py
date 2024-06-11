from unittest import TestCase
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        left = self.majority_element(nums[:half])
        right = self.majority_element(nums[half:])
        return [left, right][nums.count(right) > half]


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majority_element(self):
        answer = self.solution.majority_element([3, 2, 3])
        self.assertEqual(3, answer)

    def test_majority_element_2(self):
        answer = self.solution.majority_element([2, 2, 1, 1, 1, 2, 2])
        self.assertEqual(2, answer)

    def test_majority_element_3(self):
        answer = self.solution.majority_element([2, 3, 2, 1, 2, 1, 2])
        self.assertEqual(2, answer)
