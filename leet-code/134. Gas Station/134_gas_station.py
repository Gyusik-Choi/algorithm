from unittest import TestCase
from typing import List


class Solution:
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # i 에서 i + 1 로 이동 불가능
            if gas[i] + fuel < cost[i]:
                start = i + 1
                # i + 1 부터 재계산 될 수 있도록
                # fuel 초기화
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_complete_circuit(self):
        answer = self.solution.can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        self.assertEqual(3, answer)

    def test_can_complete_circuit_2(self):
        answer = self.solution.can_complete_circuit([2, 3, 4], [3, 4, 3])
        self.assertEqual(-1, answer)

    # 반례
    def test_can_complete_circuit_3(self):
        answer = self.solution.can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])
        self.assertEqual(4, answer)
