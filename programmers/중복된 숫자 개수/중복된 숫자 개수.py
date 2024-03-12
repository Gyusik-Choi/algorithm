def solution(array, n):
    return len(list(filter(lambda x: x == n, array)))


print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))
