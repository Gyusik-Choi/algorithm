def solution(n, left, right):
    lst = []

    for k in range(left, right + 1):
        y = k // n
        x = k % n
        lst.append(max(y + 1, x + 1))

    return lst


print(solution(3, 2, 5))
print(solution(4, 7, 14))
