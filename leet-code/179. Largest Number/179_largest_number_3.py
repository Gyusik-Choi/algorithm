from typing import List
from unittest import TestCase


class Solution:
    def __is_bigger(self, num1, num2) -> bool:
        return str(num1) + str(num2) > str(num2) + str(num1)

    # 퀵 정렬
    def __quick_sort(self, arr):
        def sort(low, high):
            if low < high:
                pivot = partition(low, high)
                sort(low, pivot - 1)
                sort(pivot + 1, high)
            return arr

        def partition(low, high):
            pivot = arr[high]
            left = low
            for right in range(low, high):
                if self.__is_bigger(arr[right], pivot):
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
            arr[left], arr[high] = arr[high], arr[left]
            return left
        return sort(0, len(arr) - 1)

    def largest_number(self, nums: List[int]) -> str:
        self.__quick_sort(nums)
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
