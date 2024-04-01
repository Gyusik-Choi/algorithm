from typing import List
from unittest import TestCase


class Solution:
    def __is_bigger(self, num1, num2) -> bool:
        return str(num1) + str(num2) > str(num2) + str(num1)

    # 병합 정렬
    def __merge_sort(self, arr):
        def sort(low, high):
            if low >= high:
                return

            mid = (low + high) // 2
            sort(low, mid)
            sort(mid + 1, high)

            l = low
            m = mid + 1
            temp = []
            while l <= mid and m <= high:
                if self.__is_bigger(arr[l], arr[m]):
                    temp.append(arr[l])
                    l += 1
                else:
                    temp.append(arr[m])
                    m += 1

            while l <= mid:
                temp.append(arr[l])
                l += 1

            while m <= high:
                temp.append(arr[m])
                m += 1

            for i in range(len(temp)):
                arr[i + low] = temp[i]

            return arr
        return sort(0, len(arr) - 1)

    def largest_number(self, nums: List[int]) -> str:
        self.__merge_sort(nums)
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
