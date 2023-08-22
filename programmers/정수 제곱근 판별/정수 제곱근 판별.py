import math


def solution(n):
    square_root = int(math.sqrt(n))

    if square_root ** 2 == n:
        return (square_root + 1) ** 2
    return -1


print(solution(121))
print(solution(3))
