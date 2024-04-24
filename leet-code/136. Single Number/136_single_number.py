from unittest import TestCase
from typing import List
from functools import reduce


class Solution:
    def single_number(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

    def single_number_ver2(self, nums: List[int]):
        return reduce(lambda acc, cur: acc ^ cur, nums)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_number(self):
        answer = self.solution.single_number([2, 2, 1])
        self.assertEqual(answer, 1)

    def test_single_number_2(self):
        answer = self.solution.single_number([4, 1, 2, 1, 2])
        self.assertEqual(answer, 4)

    def test_single_number_3(self):
        answer = self.solution.single_number([1])
        self.assertEqual(answer, 1)

    def test_single_number_ver2(self):
        answer = self.solution.single_number([2, 2, 1])
        self.assertEqual(answer, 1)

    def test_single_number_ver2_2(self):
        answer = self.solution.single_number([4, 1, 2, 1, 2])
        self.assertEqual(answer, 4)

    def test_single_number_ver2_3(self):
        answer = self.solution.single_number([1])
        self.assertEqual(answer, 1)
