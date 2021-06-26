# 풀이 1
# 반복문 형태의 팩토리얼을 이용해서
# N! // K! // (N - K)!


def factorial(n):
    num = 1
    for i in range(2, n + 1):
        num *= i
    return num


N, K = map(int, input().split())
answer = factorial(N) // factorial(K) // factorial(N - K)
print(answer)
