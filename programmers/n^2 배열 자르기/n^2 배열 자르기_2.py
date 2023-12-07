def solution(n, left, right):
    return list(map(lambda k: max(divmod(k, n)) + 1, range(left, right + 1)))


print(solution(3, 2, 5))
print(solution(4, 7, 14))
