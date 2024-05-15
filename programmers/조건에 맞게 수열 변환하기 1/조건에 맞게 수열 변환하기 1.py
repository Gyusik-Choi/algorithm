def solution(arr):
    return [num // 2 if num >= 50 and not num % 2 else num * 2 if num < 50 and num % 2 == 1 else num for num in arr]


print(solution([1, 2, 3, 100, 99, 98]))
