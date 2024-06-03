import heapq
from collections import Counter
from typing import List
from unittest import TestCase


class Solution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n + 1):
                # n + 1 만큼 counter 에서
                # 꺼내지 못하면 idle
                sub_count += 1
                result += 1

                counter[task] -= 1
                if not counter[task]:
                    del counter[task]

            if not list(filter(lambda x: x > 0, counter.values())):
                break

            result += n + 1 - sub_count

        return result


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
