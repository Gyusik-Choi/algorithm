def solution(num):
    cnt = 0

    while cnt < 500 and num != 1:
        cnt += 1

        if not num % 2:
            num //= 2
        else:
            num *= 3
            num += 1

    if num != 1:
        return -1

    return cnt


print(solution(6))
print(solution(16))
print(solution(626331))
