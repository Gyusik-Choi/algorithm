from typing import List
from unittest import TestCase


class Solution:
    def valid_utf8(self, data: List[int]) -> bool:
        # 처음에 하나 데이터 요소를 꺼낸 후
        # 해당 숫자의 이진수 앞자리 구성을 토대로
        # 앞자리 구성에 따라 봐야할 다음 바이트 갯수만큼
        # 다음 바이트의 이진수가 10 으로 시작하는지 탐색한다
        idx = 0
        while idx < len(data):
            if not self.__is_valid_first_byte(data[idx]):
                return False

            next_length = self.__get_next_byte_length(data[idx])

            for i in range(idx + 1, idx + next_length):
                # 첫번째 바이트 유형에 따라
                # 이어지는 바이트 숫자만큼
                # 검사할 수 없는 경우
                # (요소를 더 검사해야 하는데
                # 인덱스가 리스트 크기를 벗어난 상황)
                if i >= len(data):
                    return False

                if not self.__is_valid_next_utf8_byte(data[i]):
                    return False

            idx += next_length

        return True

    # 올바른 첫번째 바이트 유형인지 검사
    #
    # 첫번째 바이트는
    # 11110xxx
    # 1110xxxx
    # 110xxxxx
    # 0xxxxxxx
    # 해당 비트 유형만 올 수 있다
    # (1과 0은 비트 고정, x는 비트 변동)
    #
    # 아래와 같은 유형은 올 수 없다
    # 11111xxx
    # 10xxxxxx
    def __is_valid_first_byte(self, num):
        if num >> 3 == 0b11111:
            return False

        if num >> 6 == 0b10:
            return False

        return True

    # 첫번째 바이트 유형에 따라서
    # 추가적으로 검사해야 할
    # 이어지는 바이트 숫자
    def __get_next_byte_length(self, num) -> int:
        if num >> 3 == 0b11110:
            return 4

        if num >> 4 == 0b1110:
            return 3

        if num >> 5 == 0b110:
            return 2

        return 1

    # 첫번째 바이트 이후에
    # 이어지는 바이트가 올바른 유형인지 검사
    # 10xxxxxx 이외는 올바른 유형이 아니다
    def __is_valid_next_utf8_byte(self, num) -> bool:
        if num >> 6 == 0b10:
            return True
        return False


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_utf8(self):
        result = self.solution.valid_utf8([197, 130, 1])
        self.assertEqual(result, True)

    def test_valid_utf8_2(self):
        result = self.solution.valid_utf8([235, 140, 4])
        self.assertEqual(result, False)

    def test_valid_utf8_3(self):
        result = self.solution.valid_utf8([255])
        self.assertEqual(result, False)

    def test_valid_utf8_4(self):
        result = self.solution.valid_utf8([230, 136, 145])
        self.assertEqual(result, True)

    def test_valid_utf8_5(self):
        result = self.solution.valid_utf8([145])
        self.assertEqual(result, False)
