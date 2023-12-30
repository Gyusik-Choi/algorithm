def solution(n):
    arr = [0] * (n + 1)
    arr[1], arr[2] = 1, 2
    for i in range(3, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1000000007
    return arr[n]


print(solution(4))

