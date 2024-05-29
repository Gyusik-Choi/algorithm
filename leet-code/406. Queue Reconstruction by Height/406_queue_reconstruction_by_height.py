from typing import List
from unittest import TestCase


class Solution:
    def reconstruct_queue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in people:
            answer.insert(p[1], p)
        return answer


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reconstruct_queue(self):
        answer = self.solution.reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
        self.assertEqual(answer, [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
