import bisect
from unittest import TestCase
from typing import List


class Solution:
    def find_content_children(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_content_children(self):
        answer = self.solution.find_content_children([1, 2, 3], [1, 1])
        self.assertEqual(1, answer)

    def test_find_content_children_2(self):
        answer = self.solution.find_content_children([1, 2], [1, 2, 3])
        self.assertEqual(2, answer)

    def test_find_content_children_3(self):
        answer = self.solution.find_content_children([7, 8, 9, 10], [5, 6, 7, 8])
        self.assertEqual(2, answer)

    def test_find_content_children_4(self):
        answer = self.solution.find_content_children([5, 9, 10, 11], [5, 6, 7, 8])
        self.assertEqual(1, answer)
