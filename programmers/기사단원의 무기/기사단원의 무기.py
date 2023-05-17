import math


def get_divisor_cnt(dividend):
    # 제곱근
    sqrt = int(math.sqrt(dividend))
    divisor_cnt = 0

    for divisor in range(1, sqrt + 1):
        # 약수를 구할 수 없는 경우
        if dividend % divisor:
            continue

        quotient = dividend // divisor

        # value 와 s 가 같은 경우는
        # 약수를 구하려는 숫자의 제곱근인 경우다
        # 예를 들어 25의 제곱근은 5이고
        # 25 에서 5를 나눈 몫은 5라서
        # 이럴 경우 value 와 s 가 같다
        if quotient != divisor:
            divisor_cnt += 1

        divisor_cnt += 1

    return divisor_cnt


def solution(number, limit, power):
    divisors = []

    for i in range(1, number + 1):
        divisors.append(get_divisor_cnt(i))

    sums = 0

    for i, d in enumerate(divisors):
        if d > limit:
            sums += power
        else:
            sums += d

    return sums


print(solution(5, 3, 2))
print(solution(10, 3, 2))

