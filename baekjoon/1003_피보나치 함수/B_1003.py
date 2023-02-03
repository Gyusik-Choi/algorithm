memo = {0: 0, 1: 1}


def fibonacci(n):
    global cnt_0, cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]


T = int(input())
for t in range(T):
    cnt_0 = 0
    cnt_1 = 0
    N = int(input())
    fibonacci(N)
    print(cnt_0, cnt_1)
    # fibonacci(40)
    # if N == 0:
    #     print("1 0")
    # elif N == 1:
    #     print("0 1")
    # elif N == 2:
    #     print("1 1")
    # else:
    #     print(memo[N - 1], memo[N])

