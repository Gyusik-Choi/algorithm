from typing import List
from unittest import TestCase


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            next = intervals[i]
            if cur[1] >= next[0]:
                # cur[1] 이 next[1] 보다 클 수 있음
                # ex> [[1, 4], [2, 3]]
                if cur[1] > next[1]:
                    cur = [cur[0], cur[1]]
                else:
                    cur = [cur[0], next[1]]
            else:
                answer.append(cur)
                cur = next
        answer.append(cur)
        return answer


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        arr = self.solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        self.assertEqual(arr, [[1, 6], [8, 10], [15, 18]])

    def test_merge2(self):
        arr = self.solution.merge([[1, 4], [4, 5]])
        self.assertEqual(arr, [[1, 5]])

    def test_merge3(self):
        arr = self.solution.merge([[1, 4], [2, 3]])
        self.assertEqual(arr, [[1, 4]])
