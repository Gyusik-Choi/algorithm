from unittest import TestCase
from typing import List
import heapq


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_kth_largest(self):
        self.assertEquals(self.solution.find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
