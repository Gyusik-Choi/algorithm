from typing import List
from unittest import TestCase


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        p1, p2 = 0, 0
        answer = set()

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                answer.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1

        return list(answer)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intersection(self):
        arr = self.solution.intersection([1, 2, 2, 1], [2, 2])
        self.assertEqual(sorted(arr), [2])

    def test_intersection_2(self):
        arr = self.solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertEqual(sorted(arr), [4, 9])
