def solution(numbers):
    arr = [0, 0]
    for n in numbers:
        if arr[-1] < n:
            if arr[-2] < n:
                arr[-2], arr[-1] = n, arr[-2]
            else:
                arr[-1] = n
    return arr[-2] * arr[-1]


print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))
print(solution([2, 0, 0, 1, 1]))
