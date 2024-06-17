from unittest import TestCase
from typing import List


class Solution:
    def diff_ways_to_compute(self, expression: str) -> List[int]:
        def compute(low, high, operator):
            results = []
            for l in low:
                for h in high:
                    results.append(eval(str(l) + operator + str(h)))
            return results

        if expression.isdigit():
            return [int(expression)]

        result = []
        for idx, val in enumerate(expression):
            if val in "*-+":
                left = self.diff_ways_to_compute(expression[:idx])
                right = self.diff_ways_to_compute(expression[idx + 1:])
                result.extend(compute(left, right, val))
        return result


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_diff_ways_to_compute(self):
    #     answer = self.solution.diff_ways_to_compute("2-1-1")
    #     self.assertEqual([0, 2], sorted(answer))

    def test_diff_ways_to_compute_2(self):
        answer = self.solution.diff_ways_to_compute("2*3-4*5")
        self.assertEqual([-34, -14, -10, -10, 10], sorted(answer))
