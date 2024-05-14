from unittest import TestCase


class Solution:
    def hamming_weight(self, n: int) -> int:
        return bin(n).count('1')


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_hamming_weight(self):
        answer = self.solution.hamming_weight(11)
        self.assertEqual(answer, 3)

    def test_hamming_weight_2(self):
        answer = self.solution.hamming_weight(128)
        self.assertEqual(answer, 1)

    def test_hamming_weight_3(self):
        answer = self.solution.hamming_weight(2147483645)
        self.assertEqual(answer, 30)
