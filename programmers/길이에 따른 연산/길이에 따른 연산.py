from functools import reduce


def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else reduce(lambda acc, cur: acc * cur, num_list)


print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))
