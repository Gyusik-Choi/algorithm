def solution(arr, divisor):
    lst = sorted(list(filter(lambda num: not num % divisor, arr)))
    return lst if len(lst) else [-1]


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))

# 참고
# https://www.daleseo.com/python-filter/
