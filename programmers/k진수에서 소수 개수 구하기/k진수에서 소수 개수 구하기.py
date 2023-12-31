import math


def solution(n, k):
    def convert_to_k_digit_num(num):
        k_digit_num = ''

        while num:
            quotient, remainder = divmod(num, k)
            num = quotient
            k_digit_num += str(remainder)

        return k_digit_num[::-1]

    def is_prime_number(num):
        num = int(num)

        if num < 2:
            return False

        square_root = int(math.sqrt(num))

        for i in range(2, square_root + 1):
            if not num % i:
                return False

        return True

    cnt = 0

    for digit in convert_to_k_digit_num(n).split('0'):
        if not digit:
            continue

        if is_prime_number(digit):
            cnt += 1

    return cnt


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(10, 2))
print(solution(10, 10))
