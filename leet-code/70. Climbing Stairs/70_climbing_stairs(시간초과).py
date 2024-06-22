from unittest import TestCase


class Solution:
    def climb_stairs(self, n: int) -> int:
        cnt = 0

        def recursion(num):
            nonlocal cnt

            if num == 0:
                cnt += 1
                return

            if num == 1:
                recursion(num - 1)
            else:
                recursion(num - 1)
                recursion(num - 2)

        recursion(n)
        return cnt


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climb_stairs(self):
        answer = self.solution.climb_stairs(2)
        self.assertEqual(2, answer)

    def test_climb_stairs_2(self):
        answer = self.solution.climb_stairs(3)
        self.assertEqual(3, answer)

    def test_climb_stairs_3(self):
        answer = self.solution.climb_stairs(5)
        self.assertEqual(8, answer)
