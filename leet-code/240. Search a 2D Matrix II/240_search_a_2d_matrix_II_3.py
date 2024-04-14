from typing import List
from unittest import TestCase


class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search_matrix(self):
        answer = self.solution.search_matrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
            5)
        self.assertEqual(answer, True)

    def test_search_matrix_2(self):
        answer = self.solution.search_matrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
            20)
        self.assertEqual(answer, False)
