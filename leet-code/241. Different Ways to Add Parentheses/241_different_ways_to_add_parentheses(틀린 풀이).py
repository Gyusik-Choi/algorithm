from unittest import TestCase
from typing import List


class Solution:
    def diff_ways_to_compute(self, expression: str, results) -> List[int]:
        def compute(low, high, operator):
            result = []
            for l in low:
                for h in high:
                    result.append(eval(str(l) + operator + str(h)))
            return result

        if expression.isdigit():
            return [int(expression)]

        for idx, val in enumerate(expression):
            if val in "*-+":
                left = self.diff_ways_to_compute(expression[:idx], results)
                right = self.diff_ways_to_compute(expression[idx + 1:], results)
                results.extend(compute(left, right, val))
        return results


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_diff_ways_to_compute(self):
        answer = self.solution.diff_ways_to_compute("2-1-1", [])
        self.assertEqual([0, 2], sorted(answer))

    def test_diff_ways_to_compute_2(self):
        answer = self.solution.diff_ways_to_compute("2*3-4*5", [])
        self.assertEqual([-34, -14, -10, -10, 10], sorted(answer))
