# 그리디
def solution(n, m, section):
    cnt = 0
    wall = [False] * (n + 1)

    for start in section:
        if wall[start]:
            continue

        cnt += 1

        for end in range(start, start + m):
            if end > n:
                break

            wall[end] = True

    return cnt


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))
