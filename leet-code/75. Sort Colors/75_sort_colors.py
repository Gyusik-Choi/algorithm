from typing import List
from unittest import TestCase


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.__dnf_sort(nums)

    # 문제에서 리턴하지 말라고 해서
    # 리턴값 없이 정렬만 수행
    def __dnf_sort(self, nums: List[int]) -> None:
        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] < 1:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] > 1:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            else:
                w += 1


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sort_colors(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.solution.sort_colors(nums)
        self.assertEqual(sorted(nums), nums)

    def test_sort_colors2(self):
        nums = [2, 0, 1]
        self.solution.sort_colors(nums)
        self.assertEqual(sorted(nums), nums)
