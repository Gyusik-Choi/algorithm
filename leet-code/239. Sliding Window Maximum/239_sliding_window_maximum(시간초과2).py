from typing import List
from collections import deque
from unittest import TestCase


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        max_val = -10001
        answer = []
        deq = deque()

        for i in range(len(nums)):
            deq.append(nums[i])

            if i < k - 1:
                continue

            # if 문과 elif 문의 조건이 순서가 바뀌면 안 된다
            # nums 가 [1, 3, -1, -3, 5, 3, 6, 7] 면서
            # k 가 3인 경우
            # 1, 3, -1 이 deq 에 들어오고 나서
            # -1 이 max_val 이 된다

            if max_val == -10001:
                max_val = max(deq)
            elif nums[i] > max_val:
                max_val = nums[i]

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

    # def test_max_sliding_window_2(self):
    #     answer = self.solution.max_sliding_window([1], 1)
    #     self.assertEqual(answer, [1])
    #
    # def test_max_sliding_window_3(self):
    #     answer = self.solution.max_sliding_window([1, -1], 1)
    #     self.assertEqual(answer, [1, -1])
