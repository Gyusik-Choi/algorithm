from typing import List
from unittest import TestCase


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_info = dict()
        for num in nums1:
            nums_info[num] = 1

        for num in nums2:
            if num not in nums_info:
                continue

            nums_info[num] = 2

        return list(map(
            lambda x: x[0],
            filter(
                lambda x: x[1] == 2,
                nums_info.items())))


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intersection(self):
        arr = self.solution.intersection([1, 2, 2, 1], [2, 2])
        self.assertEqual(arr, [2])

    def test_intersection_2(self):
        arr = self.solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertEqual(arr, [4, 9])
