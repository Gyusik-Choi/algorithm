from typing import List
from unittest import TestCase


class Solution:
    def __binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if self.__binary_search(m, target):
                return True
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
        answer = self.solution.search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
        self.assertEqual(answer, False)
