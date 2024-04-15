from typing import List
from unittest import TestCase


class Solution:
    def __binary_search(self, arr: List[int], start_idx: int, target: int) -> int:
        # numbers -> [1, 2, 3, 4, 4, 9, 56, 90]
        # target -> 8
        # 위와 같은 입력인 경우
        # [4, 5] 가 정답인데 [4, 4] 가 나올 수 있다
        # 같은 인덱스가 나오지 않도록
        # left 를 0부터 시작하지 않는다
        # numbers 의 첫번째 4에서 해당 함수를 호출한 경우
        # left 를 아예 두번째 4부터 탐색할 수 있도록 한다
        # 파라미터로 start_idx 를 지정해서
        # 찾는 숫자를 대상 숫자 뒤쪽 인덱스부터 탐색한다
        left, right = start_idx, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            add_idx = self.__binary_search(numbers, idx + 1, target - num)
            if add_idx != -1:
                return [idx + 1, add_idx + 1]


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        answer = self.solution.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(answer, [1, 2])

    def test_two_sum_2(self):
        answer = self.solution.two_sum([2, 3, 4], 6)
        self.assertEqual(answer, [1, 3])

    def test_two_sum_3(self):
        answer = self.solution.two_sum([-1, 0], -1)
        self.assertEqual(answer, [1, 2])

    def test_two_sum_4(self):
        answer = self.solution.two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8)
        self.assertEqual(answer, [4, 5])
