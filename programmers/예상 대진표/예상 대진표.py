# 2 <= n <= 1048576
def solution(n, a, b):
    cnt = 0

    while True:
        if a == b:
            break

        a = (a + (a % 2)) // 2
        b = (b + (b % 2)) // 2
        cnt += 1

    return cnt


# print(solution(8, 4, 7))
# print(solution(8, 7, 8))
print(solution(8, 3, 5))
