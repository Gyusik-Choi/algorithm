from typing import List
from unittest import TestCase


class Solution:
    # 교재에 소개된 1번 풀이와 같은 방식으로 풀이 했지만
    # 현재는 리트코드에 제출하면 시간초과 발생
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(0, len(nums) - k + 1):
            answer.append(max(nums[i: i + k]))
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
