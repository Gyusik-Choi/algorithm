import operator
from unittest import TestCase


class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

    def hamming_distance_2(self, x: int, y: int) -> int:
        return bin(operator.xor(x, y)).count('1')


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_hamming_distance(self):
        self.solution.hamming_distance(1, 4)

    def test_hamming_distance_2(self):
        self.solution.hamming_distance_2(1, 4)
