def solution(n):
    cnt = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            cnt += 1

    return cnt


print(solution(5))
print(solution(6))
print(solution(5000))

# 2500
# 1250
# 625 (-1)
# 624
# 312
# 156
# 78
# 39
# 38 (-1)
# 19
# 18 (-1)
# 9
# 8 (-1)
# 4
# 2
# 1
# 0 (-1)
