def solution(n, k):
    return [i for i in range(k, n + 1, k)]


print(solution(10, 3))
print(solution(15, 5))
