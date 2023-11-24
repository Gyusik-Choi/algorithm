import math


def is_prime_number(n):
    square_root = int(math.sqrt(n))

    for num in range(2, square_root + 1):
        if not n % num:
            return False

    return True


def solution(n):
    cnt = 0

    for num in range(2, n + 1):
        if is_prime_number(num):
           cnt += 1

    return cnt


print(solution(10))
print(solution(5))
print(solution(1000000))
