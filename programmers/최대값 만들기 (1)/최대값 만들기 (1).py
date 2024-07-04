def solution(numbers):
    numbers = sorted(numbers)
    return numbers[-2] * numbers[-1]


print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))
