from unittest import TestCase
from typing import List


class Solution:
    def find_content_children(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cnt = 0
        i, j = 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
            j += 1

        return cnt


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_content_children(self):
        answer = self.solution.find_content_children([1, 2, 3], [1, 1])
        self.assertEqual(1, answer)

    def test_find_content_children_2(self):
        answer = self.solution.find_content_children([1, 2], [1, 2, 3])
        self.assertEqual(2, answer)
