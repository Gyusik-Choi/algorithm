def solution(number, n, m):
    return 1 if not number % (n * m) else 0


print(solution(60, 2, 3))
print(solution(55, 10, 5))
