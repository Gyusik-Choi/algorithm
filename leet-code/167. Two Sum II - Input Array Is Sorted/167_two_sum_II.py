from typing import List
from unittest import TestCase


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            sums = numbers[p1] + numbers[p2]
            if sums == target:
                return [p1 + 1, p2 + 1]

            if sums < target:
                p1 += 1
            else:
                p2 -= 1


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        answer = self.solution.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(answer, [1, 2])

    def test_two_sum_2(self):
        answer = self.solution.two_sum([2, 3, 4], 6)
        self.assertEqual(answer, [1, 3])

    def test_two_sum_3(self):
        answer = self.solution.two_sum([-1, 0], -1)
        self.assertEqual(answer, [1, 2])
