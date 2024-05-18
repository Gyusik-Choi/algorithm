def solution(numbers, n):
    sums = 0
    for num in numbers:
        sums += num
        if sums > n:
            break
    return sums


print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))

