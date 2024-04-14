from typing import List
from unittest import TestCase


class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] == target:
                return True

            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


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
