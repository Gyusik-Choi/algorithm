from typing import List
from collections import deque
from unittest import TestCase


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        answer = []

        deq = deque()
        # 초기값 세팅
        for i in range(k):
            if deq:
                if deq[-1] < nums[i]:
                    deq.popleft()
                    deq.append(nums[i])
            else:
                deq.append(nums[i])

        answer.append(max(deq))

        for i in range(k, len(nums)):
            if deq[-1] < nums[i]:
                deq.popleft()
                deq.append(nums[i])
            answer.append(deq[-1])

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
