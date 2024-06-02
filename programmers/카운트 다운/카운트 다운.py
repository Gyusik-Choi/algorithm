def solution(start, end_num):
    return [num for num in range(start, end_num - 1, -1)]


print(solution(10, 3))
