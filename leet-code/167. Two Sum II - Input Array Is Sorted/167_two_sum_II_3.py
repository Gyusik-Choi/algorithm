import bisect
from typing import List
from unittest import TestCase


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        for left, num in enumerate(numbers):
            right = bisect.bisect_left(numbers, target - num, left + 1)
            # bisect 모듈의 bisect_left 함수는
            # 소스코드에서 우측 끝 범위를 인자로 넣지 않으면
            # 디폴트로 우측 끝 범위를 리스트 길이로 정한다
            # 만약 찾는 숫자가 없어서 인덱스가 우측으로 벗어날 경우
            # 리스트 길이가 반환돼서 해당 값으로 인덱스 접근시 인덱스 에러가 발생할 수 있다
            # 이 에러를 막기 위해 조건문에 i 가 len(numbers) 보다 작은지 확인한다
            if right < len(numbers) and numbers[right] == target - num:
                return [left + 1, right + 1]


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
