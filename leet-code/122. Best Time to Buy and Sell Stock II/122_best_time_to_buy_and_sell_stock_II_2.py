from typing import List
from unittest import TestCase


class Solution:
    # 그리디
    # 높은 가격이 나오면 즉시 판다
    def max_profit(self, prices: List[int]) -> int:
        sums = 0
        prev = prices[0]
        for idx, price in enumerate(prices):
            if prev < price:
                sums += price - prev
            prev = price
        return sums


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        answer = self.solution.max_profit([7, 1, 5, 3, 6, 4])
        self.assertEqual(answer, 7)

    def test_max_profit_2(self):
        answer = self.solution.max_profit([1, 2, 3, 4, 5])
        self.assertEqual(answer, 4)

    def test_max_profit_3(self):
        answer = self.solution.max_profit([7, 6, 4, 3, 1])
        self.assertEqual(answer, 0)
