def count_two_power(n):
    cnt = 0
    while n >= 2:
        cnt += n // 2
        n //= 2
    return cnt


def count_five_power(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n //= 5
    return cnt


N, M = map(int, input().split())
two_power = count_two_power(N) - count_two_power(M) - count_two_power(N - M)
five_power = count_five_power(N) - count_five_power(M) - count_five_power(N - M)
print(min(two_power, five_power))
