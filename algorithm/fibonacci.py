def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    num = fibonacci(num - 1) + fibonacci(num - 2)
    return num


n = int(input())
print(fibonacci(n))
