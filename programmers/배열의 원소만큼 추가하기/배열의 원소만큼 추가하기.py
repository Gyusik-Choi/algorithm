def solution(arr):
    return [n for n in arr for _ in range(n)]


print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))
