from typing import List
from unittest import TestCase


class Solution:
    def __is_bigger(self, num1, num2) -> bool:
        return str(num1) + str(num2) < str(num2) + str(num1)

    # 삽입 정렬
    # 교재의 정렬과는 조금 다르게 구현했다
    def largest_number(self, nums: List[int]) -> str:
        for idx in range(1, len(nums)):
            i = idx
            cur_val = nums[idx]

            while i > 0 and self.__is_bigger(nums[i - 1], cur_val):
                nums[i] = nums[i - 1]
                i -= 1
            nums[i] = cur_val
        return str(int(''.join(map(str, nums))))


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_number(self):
        str_num = self.solution.largest_number([10, 2])
        self.assertEqual(str_num, '210')

    def test_largest_number_2(self):
        str_num = self.solution.largest_number([3, 30, 34, 5, 9])
        self.assertEqual(str_num, '9534330')
