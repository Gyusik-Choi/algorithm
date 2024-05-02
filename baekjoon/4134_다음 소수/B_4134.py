from math import sqrt


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if not num % i:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)


# 참고
# https://www.acmicpc.net/board/view/141180
# https://ko.wikipedia.org/wiki/%EC%86%8C%EC%88%98_(%EC%88%98%EB%A1%A0)
# https://ko.wikipedia.org/wiki/%EC%95%BD%EC%88%98
