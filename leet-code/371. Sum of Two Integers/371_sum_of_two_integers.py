

# num = int('11010', 2) & 0xF
# 11010 & 1111 -> 1010
# 교재의 초과 자리수 처리 코드는
# 최상위 비트에서 일어난 캐리를 잘라내기 위함
# 캐리를 잘라내기 위한 코드를 별도로 사용하지 않고
# 맨 마지막 캐리는 무시하면 된다
# if carry == 1: result.append('1')
# 이 코드를 그냥 작성하지 않으면 된다


# num = int('1010', 2)
# print(num ^ 0xF)
# print(~(num ^ 0xF))
# print(-(num ^ 0xF) - 1)
# answer = ~(num ^ 0xF)
# print(~answer + 1)

from unittest import TestCase


class Solution:
    def get_sum(self, a: int, b: int) -> int:
        return self.__add_by_full_adder(a, b)

    def __add_by_full_adder(self, a: int, b: int) -> int:
        # 문제의 숫자 범위는 -1000 ~ 1000 이다
        # 두 숫자의 합은
        # 최소 -2000, 최대 2000 까지 나온다
        # 2 ** 12 = 4096
        # -2048 ~ 2047
        # 12비트로 모두 나타낼 수 있어서
        # 교재의 32비트와 달리
        # 이 풀이는 12비트로 한다
        #
        # mask 는
        # 비트 자리수를 맞추기 위한 용도
        # 특정 숫자와 mask 를 and 연산하면
        # mask 의 비트와 같지 않으면
        # (mask 의 비트는 모두 1)
        # 모두 0이 된다
        #
        # mask 길이로 표현할 수 있는
        # 10진수 범위를 넘어가면 오버플로우 발생
        # 예를 들어 12비트 숫자를 다루고 싶으면
        # mask 는 0xFFF 가 된다
        # (F 는 15로 이진수로 나타내면 1111)
        #
        # 12비트는 최상위 비트를 부호 비트로 쓰는걸 제외하면
        # 11비트로 숫자를 표현한다
        # -2048 ~ 2047 까지 표현할 수 있다
        #
        # 2047 보다 큰 2048 을 mask 와 and 연산하면
        # 100000000000 이 된다
        # 이는 원래 12비트 범위에선
        # -2048 을 나타내는 값이다
        # 2047 에서 1비트 오버플로우 돼서
        # -2048 을 가리키는 값이 됐다
        # mask = 0xFFF
        # print(bin(2048 & mask))
        # print(bin(-2048 & mask))
        mask = 0xFFF
        # 2의 보수법으로 2진수를 나타낼 때 최대값
        # 12비트는 2의 보수법으로
        # -2048 ~ 2047 범위를 나타낼 수 있다
        # 0x7FF 는 12비트의 최대값인 2047이다
        # 이진수로 나타내면 011111111111다
        # 최상위 비트는 부호 비트라
        # 양수를 나타내기 위해서는
        # 최상위 비트는 0이 되어야 한다
        # 4비트에서 최상위 비트를 0으로 하고
        # 나타낼 수 있는 최대값은 0111이다
        # 0111은 10진수로 7이다
        mask_max = 0x7FF

        # mask 와 and 연산으로
        # 12비트의 길이로 비트의 길이를 제한한다
        # [2:] 로 0b 를 잘라낸다
        # zfill 로 12 길이에 모자란 만큼 앞에 0을 채운다
        a_binary = bin(a & mask)[2:].zfill(12)
        b_binary = bin(b & mask)[2:].zfill(12)

        result = []
        carry = 0

        for i in range(12):
            # 비트는 오른쪽에서 왼쪽으로 나타내기 때문에
            # 오른쪽부터 인덱스 접근한다
            a_bit = int(a_binary[11 - i])
            b_bit = int(b_binary[11 - i])

            q1 = a_bit & b_bit
            q2 = a_bit ^ b_bit
            q3 = q2 & carry
            sums = carry ^ q2
            carry = q1 | q3

            result.append(str(sums))

        result = int(''.join(result[::-1]), 2)
        if result > mask_max:
            # mask = 0xF
            # num = int('11010', 2) & mask
            # print(~(num ^ mask))
            # 비트 범위 내 (mask 의 비트 길이) 에서
            # 비트 반전 후 NOT 연산 하는데
            # 이는 1010 앞에 1 을 붙여줘서 음수로 만들기 위해서다
            # 예를 들어 총 비트가 8비트고
            # 1010 이 음수가 되려면
            # 00001010 이 아니라
            # 11111010 이 되어야 한다
            # 8비트 범위에서
            # 11111010 의 2의 보수는 00000110 이다
            # 00000110 은 +6이라서
            # 11111010 은 -6이다
            # 1010 이 -6을 나타낼 수 있도록
            # 위와 같은 연산을 한다
            result = ~(result ^ mask)
        return result


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_sum(self):
        answer = self.solution.get_sum(1, 2)
        self.assertEqual(answer, 3)

    def test_get_sum_2(self):
        answer = self.solution.get_sum(2, 3)
        self.assertEqual(answer, 5)
