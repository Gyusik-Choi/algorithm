import math


def solution(n):
    cnt = 0
    sqrt = int(math.sqrt(n))
    for num in range(1, sqrt + 1):
        if n % num:
            continue
        if n // num == num:
            cnt += 1
        else:
            cnt += 2
    return cnt


print(solution(20))
print(solution(100))
print(solution(9)) # (1, 9), (3, 3), (9, 1)
