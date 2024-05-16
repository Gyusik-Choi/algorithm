from typing import List
from collections import deque
from unittest import TestCase


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        answer = []
        deq = deque()

        for i in range(k):
            deq.append(nums[i])

        max_val = max(deq)
        answer.append(max_val)

        # nums 가 [1, -1] 이고 k 가 1인 경우
        # deq 에 1이 들어온 후
        # 비워져야 하는데 비우질 못한다

        for i in range(k, len(nums)):
            deq.append(nums[i])

            if max_val < nums[i]:
                max_val = nums[i]
            elif max_val == -10001:
                max_val = max(deq)

            answer.append(max_val)

            if max_val == deq.popleft():
                max_val = -10001

        return answer


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_sliding_window(self):
        answer = self.solution.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        self.assertEqual(answer, [3, 3, 5, 5, 6, 7])

    def test_max_sliding_window_2(self):
        answer = self.solution.max_sliding_window([1], 1)
        self.assertEqual(answer, [1])

    def test_max_sliding_window_3(self):
        answer = self.solution.max_sliding_window([1, -1], 1)
        self.assertEqual(answer, [1, -1])
