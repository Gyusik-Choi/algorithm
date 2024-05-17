from typing import List
from collections import deque
from unittest import TestCase


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        answer = []
        deq = deque()

        for i in range(len(nums)):
            if deq and deq[0] <= i - k:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)

            if i < k - 1:
                continue
            answer.append(nums[deq[0]])

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

    def test_max_sliding_window_4(self):
        answer = self.solution.max_sliding_window([7, 2, 4], 2)
        self.assertEqual(answer, [7, 4])
