from functools import reduce


def solution(box, n):
    return reduce(lambda acc, cur: acc * (cur // n), box, 1)


print(solution([1, 1, 1,], 1))
print(solution([10, 8, 6], 3))
