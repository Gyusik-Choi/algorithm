def solution(n):
    if n == 1:
        return 1

    a, b = 1, 2
    for i in range(n - 2):
        a, b = b, a + b
    return b % 1000000007


print(solution(4))

