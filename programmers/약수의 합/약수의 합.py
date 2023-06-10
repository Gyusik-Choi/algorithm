import math


def get_divisors(n):
    divisors = []
    # 제곱근
    square_root = int(math.sqrt(n))

    for root in range(1, square_root + 1):
        if not n % root:
            divisors.append(root)
            divisors.append(n // root)

    # 동일한 값이 2개가 들어갔을 경우 대비
    # 예를 들어, n 이 25 일때
    # root 가 5일 경우 5가 2개 들어간다
    return list(set(divisors))


def solution(n):
    return sum(get_divisors(n))


print(solution(12))
print(solution(5))
print(solution(25))
