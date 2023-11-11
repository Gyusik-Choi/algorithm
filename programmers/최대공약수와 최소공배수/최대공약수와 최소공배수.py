import math
from collections import Counter


def get_least_common_multiple(n, m):
    gcd = get_greatest_common_divisor(n, m)
    return gcd * (n // gcd) * (m // gcd)


def get_greatest_common_divisor(n, m):
    n_divisor = get_divisor(n)
    m_divisor = get_divisor(m)
    divisor = n_divisor + m_divisor
    counts = Counter(divisor)
    return list(filter(lambda x: x[1] > 1, counts.items()))[-1][0]


def get_divisor(n):
    divisors = set()
    square_root = int(math.sqrt(n))

    for num in range(1, square_root + 1):
        if not n % num:
            divisors.add(num)
            divisors.add(n // num)

    return sorted(list(divisors))


def solution(n, m):
    gcd = get_greatest_common_divisor(n, m)
    lcm = get_least_common_multiple(n, m)
    return [gcd, lcm]


print(solution(3, 12))
print(solution(2, 5))
