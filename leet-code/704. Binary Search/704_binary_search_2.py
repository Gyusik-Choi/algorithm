from typing import List
from unittest import TestCase


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        answer = self.solution.search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(answer, 4)

    def test_search_2(self):
        answer = self.solution.search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(answer, -1)
