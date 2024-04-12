from typing import List
from unittest import TestCase


class Solution:
    def __binary_search(self, arr, target) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        nums2 = sorted(nums2)

        for num in nums1:
            if self.__binary_search(nums2, num) == -1:
                continue
            answer.add(num)
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
