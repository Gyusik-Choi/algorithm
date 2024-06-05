from typing import List
from collections import Counter
from unittest import TestCase


class Solution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_task = counter.most_common(1)[0]
        max_idle = (max_task[1] - 1) * n
        del counter[max_task[0]]
        for i in counter.values():
            max_idle -= min(max_task[1] - 1, i)
        return len(tasks) + max(max_idle, 0)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_least_interval(self):
        answer = self.solution.least_interval(["A", "A", "A", "B", "B", "B"], 2)
        self.assertEqual(8, answer)

    def test_least_interval_2(self):
        answer = self.solution.least_interval(["A", "C", "A", "B", "D", "B"], 1)
        self.assertEqual(6, answer)

    def test_least_interval_3(self):
        answer = self.solution.least_interval(["A", "A", "A", "B", "B", "B"], 3)
        self.assertEqual(10, answer)

    def test_least_interval_4(self):
        answer = self.solution.least_interval(["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"], 4)
        self.assertEqual(10, answer)

    def test_least_interval_5(self):
        answer = self.solution.least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 1)
        self.assertEqual(12, answer)

    def test_least_interval_6(self):
        answer = self.solution.least_interval(["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2)
        self.assertEqual(12, answer)

    def test_least_interval_7(self):
        answer = self.solution.least_interval(["A", "B", "A"], 2)
        self.assertEqual(4, answer)
