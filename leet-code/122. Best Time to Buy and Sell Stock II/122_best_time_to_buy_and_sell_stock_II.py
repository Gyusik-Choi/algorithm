from typing import List
from unittest import TestCase


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        sums = 0
        prev = float('inf')
        buy = False
        # 사려면
        # 산게 없어야 하고
        # 다음 가격보다 낮은 경우
        #
        # 팔려면
        # 산게 있어야 하고
        # 다음 가격보다 높은 경우 혹은 마지막 요소인 경우
        for i in range(len(prices)):
            if prev > prices[i]:
                if buy:
                    prev = prices[i]
                else:
                    if i < len(prices) - 1 and prices[i] < prices[i + 1]:
                        buy = True
                        prev = prices[i]
            else:
                if buy:
                    if i == len(prices) - 1 or prices[i] > prices[i + 1]:
                        buy = False
                        sums += prices[i] - prev
                        prev = prices[i]
                else:
                    continue

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
