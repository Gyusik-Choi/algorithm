fibo = [0, 1]


def solution(n):
    for num in range(2, n + 1):
        fibo.append(fibo[num - 1] + fibo[num - 2])
    return fibo[n] % 1234567


print(solution(3))
