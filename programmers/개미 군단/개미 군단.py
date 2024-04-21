def solution(hp):
    cnt = 0

    cnt += hp // 5
    hp %= 5
    cnt += hp // 3
    hp %= 3
    cnt += hp // 1
    hp %= 1

    return cnt


print(solution(23))
print(solution(24))
print(solution(999))
print(solution(0))
print(solution(1000))
