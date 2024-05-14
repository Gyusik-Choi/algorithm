from unittest import TestCase


class Solution:
    # n 이 0이 될 때까지
    # n 과 n - 1 을 and 연산
    #
    # 한 이진수에서 1을 빼면
    # 하위 비트를 기준으로 1이 있는 비트까지 반전된다
    #
    # 예를 들어,
    #   10000100
    # - 00000001
    # ----------
    #   10000011
    # 이진수 10000100 에서 1을 빼면
    # 최하위 비트부터 가장 먼저 1이 나오는 6번째 비트까지 반전된다
    # 나머지 상위 비트는 그대로 유지가 된다
    # 이진수 a 와
    # 이진수 a 에서 1을 뺀 이진수 b 의
    # and 연산은 반전된 비트는 모두 0으로 변하고
    # 반전되지 않은 비트는 그대로 유지된다
    #
    # 즉, 한 이진수와 해당 이진수에서 1을 뺀 이진수의 and 연산은
    # 이진수의 1이 1개 줄어드는 결과가 나타난다
    def hamming_weight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
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
