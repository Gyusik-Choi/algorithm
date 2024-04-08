import math


def solution(n):
    return 1 if int(math.sqrt(n)) ** 2 == n else 2


print(solution(144))
print(solution(976))
