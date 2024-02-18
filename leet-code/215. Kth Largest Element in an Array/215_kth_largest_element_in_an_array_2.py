from unittest import TestCase
from typing import List
import heapq


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_kth_largest(self):
        self.assertEquals(self.solution.find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
