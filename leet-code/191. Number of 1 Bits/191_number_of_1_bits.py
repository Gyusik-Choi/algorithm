from unittest import TestCase


class Solution:
    def hamming_weight(self, n: int) -> int:
        return self.__get_cnt_of_1_bits(n)

    def __get_cnt_of_1_bits(self, n: int):
        cnt = 0
        while n:
            cnt += n % 2
            n //= 2
        return cnt


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
