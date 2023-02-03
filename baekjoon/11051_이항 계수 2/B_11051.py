def factorial(num):
    answer = 1
    if num > 1:
        for i in range(2, num + 1):
            answer *= i
    return answer


N, K = map(int, input().split())
print(factorial(N) // factorial(K) // factorial(N - K) % 10007)
