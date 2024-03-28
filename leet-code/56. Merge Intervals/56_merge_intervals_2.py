from typing import List
from unittest import TestCase


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_lst = []
        for item in sorted(intervals, key=lambda x: x[0]):
            if merged_lst and merged_lst[-1][1] >= item[0]:
                merged_lst[-1][1] = max(merged_lst[-1][1], item[1])
            else:
                merged_lst.append(item)
        return merged_lst


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        arr = self.solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        self.assertEqual(arr, [[1, 6], [8, 10], [15, 18]])

    def test_merge2(self):
        arr = self.solution.merge([[1, 4], [4, 5]])
        self.assertEqual(arr, [[1, 5]])

    def test_merge3(self):
        arr = self.solution.merge([[1, 4], [2, 3]])
        self.assertEqual(arr, [[1, 4]])
