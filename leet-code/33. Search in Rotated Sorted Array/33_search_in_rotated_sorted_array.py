from typing import List
from unittest import TestCase


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        pivot = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] == target:
                return mid_pivot

            if nums[mid_pivot] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        answer = self.solution.search([4, 5, 6, 7, 0, 1, 2], 0)
        self.assertEquals(answer, 4)
