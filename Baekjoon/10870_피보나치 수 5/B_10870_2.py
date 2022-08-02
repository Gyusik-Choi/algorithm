def fibonacci(num):
    if num == 0:
        return 0

    if num == 1 or num == 2:
        return 1

    answer = fibonacci(num - 1) + fibonacci(num - 2)
    return answer


n = int(input())
print(fibonacci(n))
