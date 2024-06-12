from unittest import TestCase
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majority_element(self):
        self.solution.majority_element([3, 2, 3])

    def test_majority_element_2(self):
        self.solution.majority_element([2, 2, 1, 1, 1, 2, 2])
