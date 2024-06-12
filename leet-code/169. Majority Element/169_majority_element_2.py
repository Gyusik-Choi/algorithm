from unittest import TestCase
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        nums_cnt = dict()
        majority_cnt = len(nums) // 2

        for num in nums:
            if num not in nums_cnt:
                nums_cnt[num] = 1
            else:
                nums_cnt[num] += 1

            if nums_cnt[num] > majority_cnt:
                return num


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majority_element(self):
        answer = self.solution.majority_element([3, 2, 3])
        self.assertEqual(3, answer)

    def test_majority_element_2(self):
        answer = self.solution.majority_element([2, 2, 1, 1, 1, 2, 2])
        self.assertEqual(2, answer)
