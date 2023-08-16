def solution(n):
    return list(map(int, str(n)[::-1]))


print(solution(12345))
