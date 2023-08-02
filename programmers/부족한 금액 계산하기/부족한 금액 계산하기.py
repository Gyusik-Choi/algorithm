def solution(price, money, count):
    sums = 0

    for i in range(1, count + 1):
        sums += price * i

    return 0 if sums <= money else sums - money
